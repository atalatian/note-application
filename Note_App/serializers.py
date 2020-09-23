from rest_framework import serializers
from .models import Notes_Record


class Note_Form_Serializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=255,
        style={"placeholder": "Title", "input_type": "text"}
    )

    note = serializers.CharField(
        style={"placeholder": "Note", "base_template": "textarea.html"},
    )


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes_Record
        fields = ["title", "note"]
