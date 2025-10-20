from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tests.models import Answer, Question, Test
from apps.tests.serializers import TestSubmissionSerializer


class TestSubmissionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TestSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            test_id = data['test_id']
            user_answers = data['answers']

            try:
                test = Test.objects.get(id=test_id)
            except Test.DoesNotExist:
                return Response(
                    {'error': 'Test not found'},
                    status=status.HTTP_404_NOT_FOUND
                )

            score = 0
            results = []

            for user_answer in user_answers:
                question_id = user_answer['question_id']
                answer_id = user_answer['answer_id']

                try:
                    question = Question.objects.get(id=question_id, test=test)
                    correct_answer = Answer.objects.get(
                        id=answer_id, question=question
                    )

                    if correct_answer.is_correct:
                        score += question.points

                    results.append(
                        {
                            'question_id': question_id,
                            'is_correct': correct_answer.is_correct,
                        }
                    )

                except (Question.DoesNotExist, Answer.DoesNotExist):
                    results.append(
                        {
                            'question_id': question_id,
                            'is_correct': False,
                            'error': 'Invalid question or answer',
                        }
                    )

            return Response(
                {'test_id': test_id, 'score': score, 'results': results},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
