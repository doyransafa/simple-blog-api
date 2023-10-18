from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=15000)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=[('technology','Technology'), ('food','Food'), ('sports','Sports')], null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.user.username}\'s post: {self.title}'
    

class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=15000)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.user.username}\'s comment on post: {self.title}'