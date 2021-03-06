# Generated by Django 4.0 on 2021-12-21 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название дисциплины')),
                ('control_form', models.CharField(choices=[('EX', 'Экзамен'), ('CR', 'Зачет'), ('TX', 'Тест')], default='CR', max_length=2, verbose_name='Форма контроля')),
                ('lecture_hours', models.PositiveIntegerField(verbose_name='Теоритические часы')),
                ('practice_hours', models.PositiveIntegerField(verbose_name='Практические часы')),
            ],
            options={
                'verbose_name': 'Учебная дисциплина',
                'verbose_name_plural': 'Учебные дисциплины',
                'db_table': 'app_discipline',
                'permissions': (('can_view_discipline_page', 'View discipline page'),),
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=100, verbose_name='Краткое название')),
                ('name', models.CharField(max_length=200, verbose_name='Полное название')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
                'db_table': 'app_faculty',
            },
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('patronymic_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Личная информация',
                'verbose_name_plural': 'Личная информация',
                'db_table': 'app_personal_info',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('study_format', models.CharField(choices=[('FT', 'Очная'), ('DS', 'Дистанционная'), ('PT', 'Очно-заочная')], default='FT', max_length=2, verbose_name='Формат обучения')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.faculty', verbose_name='Факультет')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
                'db_table': 'app_speciality',
                'unique_together': {('name', 'faculty')},
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=100, verbose_name='Краткое название')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Полное название')),
                ('creation_year', models.PositiveSmallIntegerField(verbose_name='Год образования')),
            ],
            options={
                'verbose_name': 'Университет',
                'verbose_name_plural': 'Университеты',
                'db_table': 'app_university',
            },
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.PositiveSmallIntegerField(verbose_name='Номер курса')),
                ('number', models.CharField(max_length=10, unique=True, verbose_name='Номер группы')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.speciality', verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'Учебная группа',
                'verbose_name_plural': 'Учебные группы',
                'db_table': 'app_study_group',
                'permissions': (('can_view_group_page', 'View study group page'),),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studygroup', verbose_name='Учебная группа')),
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.personalinfo', verbose_name='Личная информация')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'db_table': 'app_student',
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=30, verbose_name='Степень')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.faculty', verbose_name='Факультет')),
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.personalinfo', verbose_name='Личная информация')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'db_table': 'app_lecturer',
                'permissions': (('can_view_lecturer_page', 'View lecturer page'),),
            },
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.university', verbose_name='Университет'),
        ),
        migrations.CreateModel(
            name='SpecialityDiscipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.discipline', verbose_name='Дисциплина')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.speciality', verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'Специальность-дисциплина',
                'verbose_name_plural': 'Специальность-дисциплина',
                'db_table': 'app_speciality_discipline',
                'unique_together': {('speciality', 'discipline')},
            },
        ),
        migrations.CreateModel(
            name='LecturerGroupDiscipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.discipline', verbose_name='Дисциплина')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studygroup', verbose_name='Учебная группа')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lecturer', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Преподаватель-группа-дисциплина',
                'verbose_name_plural': 'Преподаватель-группа-дисциплина',
                'db_table': 'app_lecturer_group_discipline',
                'unique_together': {('lecturer', 'group', 'discipline')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='faculty',
            unique_together={('name', 'university')},
        ),
    ]
