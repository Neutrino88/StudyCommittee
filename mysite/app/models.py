from django.db import models


class University(models.Model):
    short_name = models.CharField('Краткое название', max_length=100)
    name = models.CharField('Полное название', max_length=200)
    creation_year = models.PositiveSmallIntegerField('Год образования')

    def __str__(self):
        return f"id {self.id}: {self.short_name}"

    def faculties(self):
        return Faculty.objects.filter(university_id=self.id)

    def specialities(self):
        return Speciality.objects.filter(faculty__university_id=self.id)

    def study_groups(self):
        return StudyGroup.objects.filter(speciality__faculty__university_id=self.id)

    def students(self):
        return Student.objects.filter(group__speciality__faculty__university_id=self.id)

    class Meta:
        db_table = 'app_university'
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'


class Faculty(models.Model):
    short_name = models.CharField('Краткое название', max_length=100)
    name = models.CharField('Полное название', max_length=200)
    university = models.ForeignKey(University, verbose_name='Университет', on_delete=models.CASCADE)

    def __str__(self):
        return f"id {self.id}: {self.short_name}"

    def specialities(self):
        return Speciality.objects.filter(faculty_id=self.id)

    def study_groups(self):
        return StudyGroup.objects.filter(speciality__faculty_id=self.id)

    def students(self):
        return Student.objects.filter(group__speciality__faculty_id=self.id)

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

    def __str__(self):
        return f"id {self.id}: {self.name} ({self.readable_study_format})"

    def students(self):
        return Student.objects.filter(group__speciality_id=self.id)

    def disciplines(self):
        disciplines_id = [sd.discipline_id for sd in SpecialityDiscipline.objects.filter(speciality_id=self.id)]
        return Discipline.objects.filter(id__in=disciplines_id)

    def study_groups(self):
        return StudyGroup.objects.filter(speciality_id=self.id)

    @property
    def readable_study_format(self):
        for s_f, readable in Speciality.STUDY_FORMAT_CHOICES:
            if s_f == self.study_format:
                return readable

    class Meta:
        db_table = 'app_speciality'
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class StudyGroup(models.Model):
    number = models.CharField('Номер группы', max_length=10)
    course_number = models.PositiveSmallIntegerField('Номер курса')
    speciality = models.ForeignKey(Speciality, verbose_name='Специальность', on_delete=models.CASCADE)

    def __str__(self):
        return f"id {self.id}: {self.number} ({self.course_number} курс)"

    def students(self):
        return Student.objects.filter(group__speciality_id=self.id)

    class Meta:
        db_table = 'app_study_group'
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'


class PersonalInfo(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    patronymic_name = models.CharField('Отчество', max_length=30)
    birthday = models.DateField('Дата рождения')

    def __str__(self):
        return f"id {self.id}: {self.full_name} ({self.birthday})"

    def readable_birthday(self):
        return self.birthday.strftime('%d %B %Y')

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic_name}"

    class Meta:
        db_table = 'app_personal_info'
        verbose_name = 'Личная информация'
        verbose_name_plural = 'Личная информация'


class Student(models.Model):
    info = models.OneToOneField(PersonalInfo, verbose_name='Личная информация', on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, verbose_name='Учебная группа', on_delete=models.CASCADE)

    def __str__(self):
        return f"id {self.id}: {self.group} - {self.info}"

    class Meta:
        db_table = 'app_student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Lecturer(models.Model):
    info = models.OneToOneField(PersonalInfo, verbose_name='Личная информация', on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, verbose_name='Факультет', on_delete=models.CASCADE)
    degree = models.CharField('Степень', max_length=30)

    def __str__(self):
        return f"id {self.id}: {self.degree} {self.info}"

    def groups_disciplines(self):
        return LecturerGroupDiscipline.objects.filter(lecturer_id=self.id)

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

    def __str__(self):
        return f"id {self.id}: {self.name} ({self.control_form}), {self.lecture_hours} л.ч., {self.practice_hours} п.ч."

    def groups_lecturers(self):
        return LecturerGroupDiscipline.objects.filter(discipline_id=self.id)

    @property
    def readable_control_form(self):
        for s_f, readable in Discipline.CONTROL_FORM_CHOICES:
            if s_f == self.control_form:
                return readable

    class Meta:
        db_table = 'app_discipline'
        verbose_name = 'Учебная дисциплина'
        verbose_name_plural = 'Учебные дисциплины'


class LecturerGroupDiscipline(models.Model):
    lecturer = models.ForeignKey(Lecturer, verbose_name='Преподаватель', on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, verbose_name='Учебная группа', on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, verbose_name='Дисциплина', on_delete=models.CASCADE)

    def __str__(self):
        names = f"{self.lecturer.info.full_name}, {self.group.number}, {self.discipline.name}"
        return f"{self.lecturer_id} {self.group_id} {self.discipline_id}: {names}"

    class Meta:
        db_table = 'app_lecturer_group_discipline'
        unique_together = ('lecturer', 'group', 'discipline')
        verbose_name = 'Преподаватель-группа-дисциплина'
        verbose_name_plural = 'Преподаватель-группа-дисциплина'


class SpecialityDiscipline(models.Model):
    speciality = models.ForeignKey(Speciality, verbose_name='Специальность', on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, verbose_name='Дисциплина', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.speciality_id} {self.discipline_id}"

    class Meta:
        db_table = 'app_speciality_discipline'
        unique_together = ('speciality', 'discipline')
        verbose_name = 'Специальность-дисциплина'
        verbose_name_plural = 'Специальность-дисциплина'
