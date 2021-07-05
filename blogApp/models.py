from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = FroalaField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args = (str(self.id)))
        return reverse('home')
