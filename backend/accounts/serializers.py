from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Review


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser

    def create(self, validated_data):
        user = super().create(validated_data)
        user.save()
        return user


class ReviewSerializers(ModelSerializer):
    class Meta:
        model = Review

    def create(self, validated_data):
        review = super().create(validated_data)
        review.save()
        return review
