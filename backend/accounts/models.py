from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils import timezone

# Create your models here.


class CustomUser(User):
    def generate_friendcode(self):
        char_list = [str(i) for i in range(10)]
        return get_random_string(10, allowed_chars=char_list)

        friendcode = models.CharField(
            max_length=10, default=self.generate_friendcode)
        score = models.IntegerField(default=100)


class Review(models.Model):
    class Meta:
        db_table = "Review"

    reviewer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="reviewer")
    reviewee = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="reviewee")
    review_text = models.CharField(max_length=255)
    review_score = models.IntegerField(default=0)
    review_time = models.DateTimeField(default=timezone.now)
