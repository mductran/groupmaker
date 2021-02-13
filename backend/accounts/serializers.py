from rest_framework.serializers import Serializer
from .models import CustomUser, Review

class UserSerializer(Serializer):
    class Meta:
        model = CustomUser
    
    def create(self, validated_data):
        user = super().create(validated_data)
        user.save()
        return user


class ReviewSerializers(Serializer):
    class Meta:
        model = Review
    
    def create(self, validated_data):
        review = super().create(validated_data)
        review.save()
        return review