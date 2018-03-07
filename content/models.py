from django.db import models


# Create your models here.
class PostItem(models.Model):
    POST_ITEM_STATUS_CHOICES = (
        ('published', 'published'),
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('archived', 'archived'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField()
    status = models.CharField(max_length=15, choices=POST_ITEM_STATUS_CHOICES)
