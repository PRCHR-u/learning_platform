from rest_framework_nested import routers
from .views import CourseViewSet, MaterialViewSet

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet, basename='courses')

courses_router = routers.NestedSimpleRouter(router, r'courses', lookup='course')
courses_router.register(r'materials', MaterialViewSet, basename='course-materials')

# The urlpatterns now only contain the router-generated URLs
urlpatterns = router.urls + courses_router.urls
