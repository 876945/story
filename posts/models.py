from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    pdf = models.FileField(upload_to='post_pdfs/', blank=True, null=True)
    
    def __str__(self):
        return self.title