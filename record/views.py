# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from record.models import StudyRecord, TestRecord
from record.serializers import StudyRecordSerializer, TestRecordSerializer


class StudyRecordList(ListCreateAPIView):
    """
    get: 학습기록 전체요청
    post: 학습기록 입력
    """
    queryset = StudyRecord.objects.all()
    serializer_class = StudyRecordSerializer


class StudyRecordDetail(RetrieveUpdateDestroyAPIView):
    """
    get: 학습기록 요청
    put: 학습기록 수정
    delete: 학습기록 삭제
    """
    queryset = StudyRecord.objects.all()
    serializer_class = StudyRecordSerializer


class TestRecordList(ListCreateAPIView):
    """
    get: 시험기록 전체요청
    post: 시험기록 입력
    """
    queryset = TestRecord.objects.all()
    serializer_class = TestRecordSerializer


class TestRecordDetail(RetrieveUpdateDestroyAPIView):
    """
    get: 시험기록 요청
    put: 시험기록 수정
    delete: 시험기록 삭제
    """
    queryset = TestRecord.objects.all()
    serializer_class = TestRecordSerializer
