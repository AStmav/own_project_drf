import uuid

from django.db import models

from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256, blank=True)
    body =RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at', '-updated_at']
    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    alt = models.CharField(max_length=200, null=True, blank=True)
    image = VersatileImageField(null=True, blank=True, upload_to='images')

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        res = ''
        if self.title:
            res = self.title
        else:
            res = self.image.url
        return res