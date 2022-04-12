from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="blog-img", null=True)
    github_url = models.URLField(max_length=100, null=True)

    class Meta:
        ordering = ["-date"]

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("blogpost-detail", args=[str(self.id)])

    def __str__(self):
        return self.title
