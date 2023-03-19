# Generated by Django 4.1.7 on 2023-03-18 06:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExamResult',
            new_name='ExamDetails',
        ),
        migrations.AlterModelOptions(
            name='examdetails',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Exam Details'},
        ),
        migrations.AlterModelOptions(
            name='objectiveexamquestions',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Exam-Objective Questions'},
        ),
    ]