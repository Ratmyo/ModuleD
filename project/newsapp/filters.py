from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):
    dateCreation_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%d-%M-%Y',
            attrs={'type': 'date'},
        ),
    )


    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'postCategory': ['exact'],
        }