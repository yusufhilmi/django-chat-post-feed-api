from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PostViewSet, UserViewSet, api_root
from rest_framework import renderers

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
})


urlpatterns=[
    path('posts/',post_list, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'), 
    path('', api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
