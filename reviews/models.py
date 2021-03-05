from django.db import models
from django.utils import timezone
# Create your models here.


class Reviews(models.Model):
    class Meta:
        db_table = "Reviews"

    RATINGS = (
        ('0.0', '0.0'), ('0.5', '0.5'),
        ('1.0', '1.0'), ('1.5', '1.5'),
        ('2.0', '2.0'), ('2.5', '2.5'),
        ('3.0', '3.0'), ('3.5', '0.5'),
        ('4.0', '4.0'), ('4.5', '4.5'),
        ('5.0', '5.0')
    )
    date = models.DateTimeField(default=timezone.now)
    score = models.FloatField(choices=RATINGS, )
    review = models.TextField(max_length=640)


class ReviewList(models.Model):
    class Meta:
        db_table = "ReviewList"

    review = models.ForeignKey('reviews.Reviews', on_delete=models.CASCADE)
    from_user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE, related_name="from_user")
    to_user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE, related_name="to_user")
