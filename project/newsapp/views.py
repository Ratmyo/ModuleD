from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import *
from .filters import PostFilter
from .forms import NewsForm, ArticlesForm
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


class PostList(LoginRequiredMixin, ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['NW'] = 'NW'
        return context


class PostSearch(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('newsapp.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('newsapp.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def get_queryset(self):
        return Post.objects.filter(categoryType='NW')


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newsapp.delete_post',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return Post.objects.filter(categoryType='NW')


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('newsapp.add_post',)
    form_class = ArticlesForm
    model = Post
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('newsapp.change_post',)
    form_class = ArticlesForm
    model = Post
    template_name = 'articles_edit.html'

    def get_queryset(self):
        return Post.objects.filter(categoryType='AR')


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newsapp.delete_post',)
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return Post.objects.filter(categoryType='AR')


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )