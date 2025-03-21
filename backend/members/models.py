from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    '''groups = models.ManyToManyField(
        'auth.Group',
        related_name='members_user_groups',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='members_user_permissions',
        blank=True
    )'''

class Member(models.Model):
  email = models.EmailField(max_length=255, default='')
  password = models.CharField(max_length=255, default='')  

class Post(models.Model):
  title = models.CharField(max_length=255, default='')
  body = models.TextField()

  def __str__(self):
    return f"Post: {self.title}"