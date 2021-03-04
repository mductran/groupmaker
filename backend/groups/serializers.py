from rest_framework.serializers import ModelSerializer
from .models import Groups, Members


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Groups

    def create(self, validated_data):
        group = super().create(validated_data)
        group.save()
        return group


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Members

    def create(self, validated_data):
        member = super().create(validated_data)
        member.save()
        return member
