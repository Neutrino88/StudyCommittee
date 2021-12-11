from django.db import models


class University(models.Model):
    name = models.CharField('Краткое название', max_length=200)
    full_name = models.CharField('Полное название', max_length=200)
    creation_year = models.DateTimeField('Год образования')

    class Meta:
        db_table = 'app_university'
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'


class Faculty(models.Model):
    name = models.CharField('Название', max_length=200)
    university = models.ForeignKey(University, verbose_name='Университет', on_delete=models.CASCADE)

    class Meta:
        db_table = 'app_faculty'
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Speciality(models.Model):
    FULL_TIME = 'FT'
    DISTANCE = 'DS'
    PART_TIME = 'PT'

    STUDY_FORMAT_CHOICES = (
        (FULL_TIME, 'Очная'),
        (DISTANCE, 'Дистанционная'),
        (PART_TIME, 'Очно-заочная'),
    )

    name = models.CharField('Название', max_length=200)
    study_format = models.CharField('Формат обучения', max_length=2, choices=STUDY_FORMAT_CHOICES, default=FULL_TIME)
    faculty = models.ForeignKey(Faculty, verbose_name='Факультет', on_delete=models.CASCADE)

    class Meta:
        db_table = 'app_speciality'
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class StudyGroup(models.Model):
    number = models.CharField('Номер группы', max_length=10)
    course_number = models.PositiveSmallIntegerField('Номер курса')
    speciality = models.ForeignKey(Speciality, verbose_name='Специальность', on_delete=models.CASCADE)

    class Meta:
        db_table = 'app_study_group'
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'


class PersonalInfo(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    patronymic_name = models.CharField('Отчество', max_length=30)
    birthday = models.DateField('Дата рождения')

    class Meta:
        db_table = 'app_personal_info'
        verbose_name = 'Личная информация'
        verbose_name_plural = 'Личная информация'


class Student(models.Model):
    info = models.OneToOneField(PersonalInfo, verbose_name='Личная информация', on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, verbose_name='Учебная группа', on_delete=models.CASCADE)

    class Meta:
        db_table = 'app_student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Lecturer(models.Model):
    info = models.OneToOneField(PersonalInfo, verbose_name='Личная информация', on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, verbose_name='Факультет', on_delete=models.CASCADE)
    degree = models.CharField('Степень', max_length=30)

    class Meta:
        db_table = 'app_lecturer'
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Discipline(models.Model):
    EXAM = 'EX'
    CREDIT = 'CR'
    TEST = 'TX'

    CONTROL_FORM_CHOICES = (
        (EXAM, 'Экзамен'),
        (CREDIT, 'Зачет'),
        (TEST, 'Тест'),
    )

    name = models.CharField('Название дисциплины', max_length=200)
    control_form = models.CharField('Форма контроля', max_length=2, choices=CONTROL_FORM_CHOICES, default=CREDIT)
    lecture_hours = models.PositiveIntegerField('Теоритические часы')
    practice_hours = models.PositiveIntegerField('Практические часы')

    class Meta:
        db_table = 'app_discipline'
        verbose_name = 'Учебная дисциплина'
        verbose_name_plural = 'Учебные дисциплины'


class LecturerGroupDiscipline(models.Model):
    professor = models.ForeignKey(Lecturer, verbose_name='Преподаватель', on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, verbose_name='Учебная группа', on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, verbose_name='Дисциплина', on_delete=models.CASCADE)

    class Meta:
        db_table = 'app_lecturer_group_discipline'
        unique_together = ('professor', 'group', 'discipline')
        verbose_name = 'Преподаватель-группа-дисциплина'
        verbose_name_plural = 'Преподаватель-группа-дисциплина'


class SpecialityDiscipline(models.Model):
    speciality = models.ForeignKey(Speciality, verbose_name='Специальность', on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, verbose_name='Дисциплина', on_delete=models.CASCADE)

    class Meta:
        db_table = 'app_speciality_discipline'
        unique_together = ('speciality', 'discipline')
        verbose_name = 'Специальность-дисциплина'
        verbose_name_plural = 'Специальность-дисциплина'
