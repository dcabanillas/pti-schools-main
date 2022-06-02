# Generated by Django 4.0.3 on 2022-04-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday')], db_index=True, default='MONDAY', max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='month_days',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='week_days',
        ),
        migrations.AddField(
            model_name='schedule',
            name='week_days',
            field=models.ManyToManyField(to='schools.day'),
        ),
    ]