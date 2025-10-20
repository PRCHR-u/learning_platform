from django.urls import path

from apps.tests.views import TestSubmissionAPIView

urlpatterns = [path('submit/', TestSubmissionAPIView.as_view(), name='test-submission')]
