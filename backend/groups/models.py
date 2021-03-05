from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Groups(models.Model):
    # TODO: add group photo
    class Meta:
        db_table = "Groups"

    name = models.CharField(max_length=255)
    member_count = models.IntegerField(default=0)
    description = models.CharField(max_length=255)


class Members(models.Model):
    class Meta:
        db_table = "Members"

    class UserRoleChoices(models.TextChoices):
        member = 'MEM', _('Member')
        leader = 'LEA', _('Leader')

    member = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=3, choices=UserRoleChoices.choices, default=UserRoleChoices.member)


class TaskList(models.Model):
    class Meta:
        db_table = "TaskList"

    group = models.ForeignKey('groups.Groups', on_delete=models.CASCADE)
    task = models.ForeignKey('tasks.Tasks', on_delete=models.CASCADE)
