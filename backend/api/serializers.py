from rest_framework import serializers
from .models import Post, Comment, User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username')

class PostSerializer(serializers.ModelSerializer):

  user = UserSerializer()

  class Meta:
    model = Post
    fields = '__all__'

  def create(self, validated_data):
    validated_data['user'] = self.context['request'].user
    return Post.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):

  user = UserSerializer()
  # post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
  
  class Meta:
    model = Comment
    # exclude = ['post']
    fields = '__all__'
  
  def create(self, validated_data):
    validated_data['user'] = self.context['request'].user
    return Post.objects.create(**validated_data)

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
    )

  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = User
    fields = ('username', 'password', 'password2', 'email')

  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError({"password": "Password fields didn't match."})

    return attrs

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
    )

    user.set_password(validated_data['password'])
    user.save()

    return user