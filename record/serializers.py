from rest_framework.serializers import ModelSerializer

from .models import StudyRecord, TestRecord


class StudyRecordSerializer(ModelSerializer):
    class Meta:
        model = StudyRecord
        fields = ('id', 'user', 'note', 'step', 'unknownwords', 'regdate',)


class TestRecordSerializer(ModelSerializer):
    class Meta:
        model = TestRecord
        fields = ('id', 'user', 'note', 'score', 'regdate',)
