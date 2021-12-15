from django.contrib import admin
from app import models


admin.site.site_header = 'Панель администратора Учебного комитета'
admin.site.site_title = 'Учебный комитет'

admin.site.register(models.Lecturer)
admin.site.register(models.Discipline)
admin.site.register(models.StudyGroup)
admin.site.register(models.Faculty)
admin.site.register(models.Speciality)
admin.site.register(models.University)
admin.site.register(models.PersonalInfo)
admin.site.register(models.LecturerGroupDiscipline)
admin.site.register(models.Student)
admin.site.register(models.SpecialityDiscipline)
