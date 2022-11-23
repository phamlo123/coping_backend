from django.db import models

class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    content = models.CharField(max_length=1000)
    #TODO: take care of tags
    tags = models.CharField(max_length=10)


    def __str__(self) -> str:
        return f"{self.title}"