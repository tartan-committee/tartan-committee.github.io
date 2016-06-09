from django.utils import timezone
from django.db import models

# Create your models here.

class Member(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=40)
    andrew_id = models.CharField(max_length=10)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.user