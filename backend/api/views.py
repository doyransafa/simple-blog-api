from rest_framework import generics
from .models import Post, Comment, User
from .serializers import PostCreateSerializer, PostRetrieveSerializer, CommentCreateSerializer, CommentRetreiveSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer

class PostList(generics.ListAPIView):
	serializer_class = PostRetrieveSerializer

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
	

class PostDetail(generics.RetrieveDestroyAPIView):

	queryset = Post.objects.all()
	serializer_class = PostRetrieveSerializer

class PostCreateView(generics.CreateAPIView):

	queryset = Post.objects.all()
	serializer_class = PostCreateSerializer

class PostUpdateView(generics.UpdateAPIView):

	queryset = Post.objects.all()
	serializer_class = PostCreateSerializer

class CommentList(generics.ListCreateAPIView):

	queryset = Comment.objects.all()
	serializer_class = CommentRetreiveSerializer

	def get_object(self, queryset=None, **kwargs):
		post = self.kwargs.get('post_id')
		return Comment.objects.filter(post=post)

class CommentDetail(generics.RetrieveDestroyAPIView):

	queryset = Comment.objects.all()
	serializer_class = CommentRetreiveSerializer

class CommentCreateView(generics.CreateAPIView):
	
	queryset = Comment.objects.all()
	serializer_class = CommentCreateSerializer