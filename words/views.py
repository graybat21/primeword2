from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from .serializers import TextbookSerializer, NoteSerializer, WordSerializer
from .models import Textbook, Note, Word


class TextbookViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = TextbookSerializer
    queryset = Textbook.objects.all()


class NoteViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

# class NoteListByProfileViewSet(ListAPIView):
#     serializer_class = NoteSerializer
#     queryset = Note.objects.filter()


class WordViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all()
