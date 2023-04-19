# Generated by Django 4.2 on 2023-04-17 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Elearning_app', '0009_alter_course_categoryid_alter_lesson_courseid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]
