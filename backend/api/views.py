from rest_framework import generics
from .models import Post, Comment, User
from .serializers import PostSerializer, CommentSerializer, RegisterSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission

# Create your views here.

class UserUpdatePermission(BasePermission):
	message = 'You cannot Update or Delete a post that is not yours!'

	def has_object_permission(self, request, view, obj):
		
		if request.method in SAFE_METHODS:
			return True
		
		return obj.user == request.user

class PostList(generics.ListCreateAPIView):
	serializer_class = PostSerializer

	def get_queryset(self):

		user = self.request.query_params.get('user')
		search = self.request.query_params.get('search', '')
		category = self.request.query_params.get('category', '')

		queryset = Post.objects.all()

		if user:
			queryset = queryset.filter(user__username=user)
		if search:
			queryset = queryset.filter(title__icontains=search)
		if category:
			queryset = queryset.filter(category=category)

		return queryset
	

class PostDetail(generics.RetrieveUpdateDestroyAPIView, UserUpdatePermission):
	permission_classes = [UserUpdatePermission]
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class CommentList(generics.ListCreateAPIView):

	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def get_object(self, queryset=None, **kwargs):
		post = self.kwargs.get('post_id')
		return Comment.objects.filter(post=post)

class CommentDetail(generics.RetrieveDestroyAPIView):
	permission_classes = [UserUpdatePermission]
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = RegisterSerializer
