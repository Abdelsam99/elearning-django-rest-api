# Generated by Django 4.2 on 2023-04-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_app', '0005_notice_course_notice_date_alter_lesson_video_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answernotice',
            options={'verbose_name_plural': 'AnswerNotice'},
        ),
        migrations.AlterField(
            model_name='notice',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
