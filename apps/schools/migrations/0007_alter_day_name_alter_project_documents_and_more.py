# Generated by Django 4.0.3 on 2022-04-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_rename_specialties_teacher_specialities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='name',
            field=models.CharField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], db_index=True, default='MONDAY', max_length=10),
        ),
        migrations.AlterField(
            model_name='project',
            name='documents',
            field=models.ManyToManyField(blank=True, null=True, to='schools.document'),
        ),
        migrations.AlterField(
            model_name='project',
            name='schedules',
            field=models.ManyToManyField(blank=True, null=True, to='schools.schedule'),
        ),
        migrations.AlterField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='schools.skill'),
        ),
        migrations.AlterField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='schools.student'),
        ),
        migrations.AlterField(
            model_name='project',
            name='teachers',
            field=models.ManyToManyField(blank=True, null=True, to='schools.teacher'),
        ),
        migrations.AlterField(
            model_name='student',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, to='schools.group'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='teachers'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='specialities',
            field=models.ManyToManyField(blank=True, null=True, to='schools.speciality'),
        ),
    ]
