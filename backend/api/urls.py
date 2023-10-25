from django.urls import path
from .views import PostList, PostDetail, CommentList, CommentCreateView, CommentDetail, MyTokenObtainPairView, PostCreateView, PostUpdateView
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
  openapi.Info(
    title="Simple Blog API",
    default_version='v1',
    description="kg baba",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="contact@snippets.local"),
    license=openapi.License(name="BSD License"),
  ),
  public=True,
  permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
  path('posts', PostList.as_view(), name='post_list'),
  path('post/<int:pk>', PostDetail.as_view(), name='post_details'),
  path('post/create', PostCreateView.as_view(), name='post_create'),
  path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
  path('post/<int:post_id>/comments', CommentList.as_view(), name='comment_list'),
  path('comment/create', CommentCreateView.as_view(), name='comment_create'),
  path('comment/<int:pk>', CommentDetail.as_view(), name='comment_details'),
  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

  #documentation
  path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
