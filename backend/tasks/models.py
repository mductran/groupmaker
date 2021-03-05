from django.db import models
from django.utils import timezone

# Create your models here.
class Tasks(models.Model):
    class Meta:
        db_table = "Tasks"
    
    creator = models.ForeignKey('accounts.Users', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(default=timezone.now)


class AssignedUsers(models.Model):
    class Meta:
        db_table = "AssignedUsers"
    
    worker = models.ForeignKey('accounts.Users', on_delete=models.CASCADE)
    task = models.ForeignKey('tasks.Tasks', on_delete=models.CASCADE)

