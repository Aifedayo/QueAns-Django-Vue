from rest_framework import serializers

from questions.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        exclude = ['updated_at']
