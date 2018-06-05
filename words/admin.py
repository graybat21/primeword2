from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin

from .models import Textbook, Note, Word


class WordResource(resources.ModelResource):
    class Meta:
        model = Word
        # import_id_fields = ('word_id',)
        # exclude = ('word_id',)


# Register your models here.
class TextbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'grade', 'school_code', 'academy_code', 'regdate')
    list_display_links = list_display


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'textbook', 'lesson', 'regdate')
    list_display_links = list_display


# class WordclassAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'memo')
#     list_display_links = list_display


class WordAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'spelling', 'memo', 'note', 'meaning')
    list_display_links = list_display
    resource_class = WordResource


admin.site.register(Textbook, TextbookAdmin)
admin.site.register(Note, NoteAdmin)
# admin.site.register(Wordclass, WordclassAdmin)
admin.site.register(Word, WordAdmin)
