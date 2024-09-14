import uuid
from django.db import models

class File(models.Model):
    title = models.CharField(max_length=256, default='No title')
    file = models.FileField(upload_to='files')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.title

# Create your models here.
