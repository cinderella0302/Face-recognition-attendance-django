# Generated by Django 4.2.6 on 2023-10-26 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_student_profile_pic_profileimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileimage',
            old_name='profile_pic',
            new_name='profile_picture',
        ),
    ]
