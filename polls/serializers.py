from rest_framework import serializers
from .models import Questions


class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id', 'question_text', 'pub_date')


