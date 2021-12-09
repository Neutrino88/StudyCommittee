from django.db import models


class University(models.Model):
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    creation_year = models.DateTimeField('Год образования')

    class Meta:
        db_table = 'university'


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    class Meta:
        db_table = 'faculty'


class Speciality(models.Model):
    FULL_TIME = 'FT'
    DISTANCE = 'DS'
    PART_TIME = 'PT'

    STUDY_FORMAT_CHOICES = (
        (FULL_TIME, 'Очное'),
        (DISTANCE, 'Дистанционное'),
        (PART_TIME, 'Очно-заочное'),
    )

    name = models.CharField(max_length=200)
    study_format = models.CharField(max_length=2, choices=STUDY_FORMAT_CHOICES, default=FULL_TIME)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        db_table = 'speciality'


class StudyGroup(models.Model):
    number = models.CharField(max_length=10)
    course_number = models.PositiveIntegerField()
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    class Meta:
        db_table = 'study_group'


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic_name = models.CharField(max_length=30)
    birthday = models.DateField()

    class Meta:
        db_table = 'personal_info'


class Student(models.Model):
    info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student'


class Lecturer(models.Model):
    info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    degree = models.CharField(max_length=30)

    class Meta:
        db_table = 'lecturer'


class Discipline(models.Model):
    EXAM = 'EX'
    CREDIT = 'CR'
    TEST = 'TX'

    CONTROL_FORM_CHOICES = (
        (EXAM, 'Экзамен'),
        (CREDIT, 'Зачет'),
        (TEST, 'Тест'),
    )

    name = models.CharField(max_length=200)
    control_form = models.CharField(max_length=2, choices=CONTROL_FORM_CHOICES, default=CREDIT)
    lecture_hours = models.PositiveIntegerField()
    practice_hours = models.PositiveIntegerField()

    class Meta:
        db_table = 'discipline'


class LecturerGroupDiscipline(models.Model):
    professor = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    class Meta:
        db_table = 'lecturer_group_discipline'
        unique_together = ('professor', 'group', 'discipline')


class SpecialityDiscipline(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    class Meta:
        db_table = 'speciality_discipline'
        unique_together = ('speciality', 'discipline')
