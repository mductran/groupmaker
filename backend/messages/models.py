from django.db import models
from django.utils import timezone

# Create your models here.


class Messages(models.Model):
    class Meta:
        db_table = "Messages"
        abstract = True

    sender = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE, related_name="receiver")
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)


class Requests(Messages):
    class Meta(Messages.Meta):
        db_table = "Requests"

    posts = models.ForeignKey('posts.Posts', on_delete=models.CASCADE)
