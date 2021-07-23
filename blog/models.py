from django.db import models


# post
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author

    def __str__(self):
        return '[{0}] {1}'.format(self.pk, self.title)

    def get_absolute_url(self):
        return '/blog/{0}'.format(self.pk)

