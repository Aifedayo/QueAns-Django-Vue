from rest_framework import viewsets
from questions.models import Question
from questions.api.serializers import QuestionSerializer
from rest_framework.permissions import IsAuthenticated

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        