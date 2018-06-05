from django.contrib import admin

# Register your models here.
from record.models import StudyRecord, TestRecord


class StudyRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'note', 'step', 'unknownwords', 'regdate')
    list_display_links = list_display


class TestRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'note', 'score', 'regdate')
    list_display_links = list_display


admin.site.register(StudyRecord, StudyRecordAdmin)
admin.site.register(TestRecord, TestRecordAdmin)
