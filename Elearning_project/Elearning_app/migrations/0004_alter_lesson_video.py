# Generated by Django 4.2 on 2023-04-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_app', '0003_remove_lesson_categoryid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.FileField(upload_to='lessonvideos/'),
        ),
    ]