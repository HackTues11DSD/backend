from django.db import models

class Member(models.Model):
  email = models.EmailField(max_length=255, default='')
  password = models.CharField(max_length=255, default='')  

class Post(models.Model):
  title = models.CharField(max_length=255, default='')
  body = models.TextField()

  def __str__(self):
    return f"Post: {self.title}"