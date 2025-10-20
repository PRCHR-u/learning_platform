from rest_framework import serializers

from apps.tests.models import Answer, Question, Test


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'points', 'answers']


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ['id', 'title', 'max_score', 'created_at', 'questions']


class UserAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_id = serializers.IntegerField()


class TestSubmissionSerializer(serializers.Serializer):
    test_id = serializers.IntegerField()
    answers = UserAnswerSerializer(many=True)
