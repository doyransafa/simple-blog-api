from django.urls import path, re_path
from django.urls import re_path as url
from .views import PostList, PostDetail, CommentList, CommentDetail

urlpatterns = [
    path('posts', PostList.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_details'),
    path('post_comments/<int:post_id>', CommentList.as_view(), name='comment_list'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comment_details'),

]
