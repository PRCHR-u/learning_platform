from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.courses.models import Course, Material
from apps.users.models import User


class CourseAPITests(APITestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(
            username='teacher', email='teacher@example.com',
            password='password123', role='teacher'
        )
        self.student = User.objects.create_user(
            username='student', email='student@example.com',
            password='password123', role='student'
        )

        self.course = Course.objects.create(
            title='Test Course',
            description='Course Description',
            owner=self.teacher
        )
        self.course_list_url = reverse('course-list')
        self.course_detail_url = reverse(
            'course-detail', kwargs={'pk': self.course.pk}
        )

    def test_teacher_can_create_course(self):
        self.client.force_authenticate(user=self.teacher)
        data = {
            'title': 'New Course',
            'description': 'A new course description.'
        }
        response = self.client.post(self.course_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_student_cannot_create_course(self):
        self.client.force_authenticate(user=self.student)
        data = {
            'title': 'New Course',
            'description': 'A new course description.'
        }
        response = self.client.post(self.course_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_owner_can_edit_course(self):
        self.client.force_authenticate(user=self.teacher)
        data = {'title': 'Updated Course Title'}
        response = self.client.patch(
            self.course_detail_url, data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_user_cannot_edit_course(self):
        self.client.force_authenticate(user=self.student)
        data = {'title': 'Updated Course Title'}
        response = self.client.patch(
            self.course_detail_url, data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class MaterialAPITests(APITestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(
            username='teacher', email='teacher@example.com',
            password='password123', role='teacher'
        )
        self.student = User.objects.create_user(
            username='student', email='student@example.com',
            password='password123', role='student'
        )
        self.other_teacher = User.objects.create_user(
            username='other_teacher', email='other@example.com',
            password='password123', role='teacher'
        )

        self.course = Course.objects.create(
            title='Test Course',
            description='A description',
            owner=self.teacher
        )
        self.material = Material.objects.create(
            course=self.course, title='Test Material', order=1
        )
        self.material_list_url = reverse(
            'course-materials-list', kwargs={'course_pk': self.course.pk}
        )
        self.material_detail_url = reverse(
            'course-materials-detail',
            kwargs={'course_pk': self.course.pk, 'pk': self.material.pk}
        )

    def test_teacher_can_create_material(self):
        self.client.force_authenticate(user=self.teacher)
        data = {'title': 'New Material', 'order': 2}
        response = self.client.post(
            self.material_list_url, data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_student_cannot_create_material(self):
        self.client.force_authenticate(user=self.student)
        data = {'title': 'New Material', 'order': 2}
        response = self.client.post(
            self.material_list_url, data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_owner_can_edit_material(self):
        self.client.force_authenticate(user=self.teacher)
        data = {'title': 'Updated Material'}
        response = self.client.patch(
            self.material_detail_url, data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_user_cannot_edit_material(self):
        self.client.force_authenticate(user=self.other_teacher)
        data = {'title': 'Updated Material'}
        response = self.client.patch(
            self.material_detail_url, data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
