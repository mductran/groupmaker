from django.db import models
from django.utils import timezone

# Create your models here.


class Posts(models.Model):
    class Meta:
        db_table = "Posts"

    poster = models.ForeignKey('accounts.Users', on_delete=models.CASCADE)
    group = models.ForeignKey('groups.Groups', on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    description = models.TextField(max_length=640)
    date = models.DateTimeField(default=timezone.now)
