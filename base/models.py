from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=600)
    body = models.TextField()
    image = models.ImageField(default="hr-1.jpg", upload_to='uploads/articles')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField()

    def __str__(self):
        return self.email

