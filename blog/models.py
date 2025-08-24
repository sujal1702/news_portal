from django.db import models
from django.utils.text import slugify


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Post Model
  # at the top if not already

from django.utils.text import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True) 
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title 



    # Feedback Model
class Feedback(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='feedbacks')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)

 # blog/models.py
from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
   


# Ad Model
class Ad(models.Model):
    title = models.CharField(max_length=200, default='Untitled Ad')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='ads/')
    link = models.URLField(default='#')

    def __str__(self):
        return f"Ad {self.id}"


# Subscriber Model
class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



