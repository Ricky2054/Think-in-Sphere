# Generated by Django 4.1.7 on 2023-03-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_examdetails_exam_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examdetails',
            name='exam_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='examdetails',
            name='time_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='examdetails',
            name='user_marks',
            field=models.IntegerField(default=0),
        ),
    ]
