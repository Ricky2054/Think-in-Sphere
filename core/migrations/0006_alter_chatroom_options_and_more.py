# Generated by Django 4.1.7 on 2023-03-04 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_chatroom_room_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatroom',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Chat Rooms'},
        ),
        migrations.AlterModelOptions(
            name='userrequesthistory',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'User Search History'},
        ),
    ]
