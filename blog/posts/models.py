from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=400)
    summary = models.CharField(max_length=150)
    category = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    # created_date = models.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    published_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id}: {self.title}"


class Author(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    posts = models.ManyToManyField(Post, blank=True, related_name="authors")
    def __str__(self):
        return f"{self.first} {self.last}"