from django.db import models
from .post import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="post_comments")
    owner = models.ForeignKey('auth.User', related_name="user_comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)