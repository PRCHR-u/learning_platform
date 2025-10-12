from rest_framework import serializers
from .models import Course, Material


class MaterialSerializer(serializers.ModelSerializer):
    file = serializers.URLField(max_length=200, required=False)

    class Meta:
        model = Material
        fields = ('id', 'course', 'title', 'file', 'order')
        read_only_fields = ('course',)


class CourseSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'owner', 'title', 'description', 'materials')
        read_only_fields = ('owner',)
