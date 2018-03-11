from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


# Create your models here.
class PostItem(models.Model):
    POST_ITEM_STATUS_CHOICES = (
        ('published', 'Published'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('archived', 'Archived'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField()
    status = models.CharField(max_length=15, choices=POST_ITEM_STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{} : {}".format(self.title, self.status)
