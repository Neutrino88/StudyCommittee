from django.contrib import admin
from app import models


admin.site.site_header = 'Панель администратора Учебного комитета'
admin.site.site_title = 'Учебный комитет'

admin.site.register(models.Lecturer)
admin.site.register(models.Discipline)
admin.site.register(models.LecturerGroupDiscipline)
admin.site.register(models.Student)
admin.site.register(models.SpecialityDiscipline)


@admin.register(models.University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'id', 'name', 'creation_year')


@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'id', 'name')


@admin.register(models.Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'readable_study_format')


@admin.register(models.StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ('number', 'id', 'course_number')


@admin.register(models.PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birthday')
