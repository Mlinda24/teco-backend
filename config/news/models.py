from django.db import models
# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="Unique URL friendly name (e.g., water-project-2026)")
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    excerpt = models.TextField(help_text="Short summary for the home page")
    content = models.TextField(help_text="Full article content")
    published_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title