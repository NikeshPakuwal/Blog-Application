from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = FroalaField()

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)