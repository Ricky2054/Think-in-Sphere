# Generated by Django 4.1.7 on 2023-03-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_otp_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('hi', 'Hindi'), ('ben', 'Bengali')], default='en', max_length=255),
        ),
    ]
