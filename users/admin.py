from django.contrib import admin
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportMixin

from users.models import Profile, SchoolGroup, AcademyGroup


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'grade', 'school_code',)
    list_display_links = list_display


class SchoolGroupResource(resources.ModelResource):
    class Meta:
        model = SchoolGroup
        # import_id_fields = ('word_id',)
        # exclude = ('word_id',)


class AcademyGroupAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('code', 'name',)
    list_display_links = list_display


class SchoolGroupAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('code', 'name',)
    list_display_links = list_display
    resource_class = SchoolGroupResource


admin.site.register(Profile, ProfileAdmin)
admin.site.register(SchoolGroup, SchoolGroupAdmin)
admin.site.register(AcademyGroup, AcademyGroupAdmin)
