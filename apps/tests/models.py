from django.db import models

from apps.courses.models import Material


class Test(models.Model):
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name='tests'
    )
    title = models.CharField(max_length=200)
    max_score = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name='questions'
    )
    text = models.TextField()
    points = models.IntegerField(default=10)


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers'
    )
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
