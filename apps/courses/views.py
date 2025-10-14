from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Course, Material
from .serializers import CourseSerializer, MaterialSerializer
from .permissions import IsOwner, IsTeacher, IsMaterialCourseOwner


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsTeacher]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get_queryset(self):
        return Material.objects.filter(course_id=self.kwargs['course_pk'])

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsTeacher, IsMaterialCourseOwner]
        else:
            permission_classes = [IsMaterialCourseOwner]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        course = Course.objects.get(pk=self.kwargs['course_pk'])
        serializer.save(course=course)
