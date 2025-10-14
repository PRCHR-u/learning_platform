from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Course, Material
from .serializers import CourseSerializer, MaterialSerializer
from .permissions import IsOwner, IsTeacher, IsMaterialCourseOwner
from rest_framework.views import APIView
from rest_framework.response import Response

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


class TeacherDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        user = request.user
        # NOTE: Using hardcoded data as per the user's suggestion for now.
        # In a real application, this would be calculated based on the user.
        return Response({
            'total_students': 1247,
            'active_courses': 8,
            'monthly_income': "184,500",
            'rating': 4.8,
            'recent_activities': [
                {
                    'icon': 'student',
                    'title': 'Мария Петрова',
                    'description': 'Завершила курс "Python для начинающих"',
                    'time': '2 часа назад'
                },
                {
                    'icon': 'payment',
                    'title': 'Новый платеж',
                    'description': 'Иван Сидоров оплатил курс "Веб-разработка"',
                    'time': '5 часов назад'
                },
                {
                    'icon': 'course',
                    'title': 'Новый студент',
                    'description': 'Анна Козлова записалась на "Data Science"',
                    'time': 'Вчера'
                },
            ]
        })
