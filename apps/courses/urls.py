from django.urls import path
from rest_framework_nested import routers
from .views import CourseViewSet, MaterialViewSet, TeacherDashboardAPIView

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet, basename='courses')

courses_router = routers.NestedSimpleRouter(router, r'courses', lookup='course')
courses_router.register(r'materials', MaterialViewSet, basename='course-materials')

# Combine router URLs with the custom dashboard URL
urlpatterns = router.urls + courses_router.urls + [
    path('teacher/dashboard/', TeacherDashboardAPIView.as_view(), name='teacher-dashboard'),
]
