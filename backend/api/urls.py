from django.urls import path
from .views import PostList, PostDetail, CommentList, CommentCreateView, CommentDetail, MyTokenObtainPairView, PostCreateView, PostUpdateView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('posts', PostList.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_details'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:post_id>/comments', CommentList.as_view(), name='comment_list'),
    path('comment/create', CommentCreateView.as_view(), name='comment_details'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comment_details'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
