from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Исправленный импорт, указывающий на приложение courses
from apps.courses.permissions import IsTeacher


class TeacherDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        # NOTE: The data is hardcoded as per the user's request for a
        # quick demo. In a real application, this would be calculated
        # from the database.
        return Response({
            'total_students': 1247,
            'active_courses': 8,
            'monthly_income': 184500,
            'rating': 4.8,
            'recent_activities': [
                {
                    'type': 'completion',
                    'student': 'Мария Петрова',
                    'course': 'Python для начинающих',
                    'time': '2 часа назад'
                },
                {
                    'type': 'payment',
                    'student': 'Иван Сидоров',
                    'course': 'Веб-разработка',
                    'time': '5 часов назад'
                },
                {
                    'type': 'enrollment',
                    'student': 'Анна Козлова',
                    'course': 'Data Science',
                    'time': 'Вчера'
                },
            ]
        })
