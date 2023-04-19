# Generated by Django 4.2 on 2023-04-14 13:50

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Elearning_app', '0004_alter_lesson_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Elearning_app.course'),
        ),
        migrations.AddField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 4, 14, 13, 50, 40, 381751, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.FileField(upload_to='lessonvideos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])]),
        ),
        migrations.AlterField(
            model_name='notice',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AnswerNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Elearning_app.course')),
                ('notice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Elearning_app.notice')),
            ],
            options={
                'verbose_name_plural': 'Notices',
            },
        ),
    ]
