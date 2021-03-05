from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils import timezone

# Create your models here.


class Users(User):
    # TODO: add user profile pic
    class Meta:
        db_table = "User"

    def generate_friendcode(self):
        char_list = [str(i) for i in range(10)]
        return get_random_string(10, allowed_chars=char_list)

    friendcode = models.CharField(
        max_length=10, default=generate_friendcode)
    rating = models.FloatField(default=0.0)
