from django.urls import path, include
from rest_framework_nested import routers
from .views import CourseViewSet, MaterialViewSet

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet, basename='course')

courses_router = routers.NestedSimpleRouter(
    router, r'courses', lookup='course'
)
courses_router.register(
    r'materials', MaterialViewSet, basename='course-materials'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(courses_router.urls)),
]
