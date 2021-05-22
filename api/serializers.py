from rest_framework import serializers
from .models import Note
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'author', 'username', 'link', 'date_field')



       