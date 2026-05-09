from django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    cover_image = models.ImageField(upload_to='post_covers/', blank=True, null=True)
    author = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

def __str__(self):
        return self.title

