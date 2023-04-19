# Generated by Django 4.2 on 2023-04-17 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Elearning_app', '0008_alter_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='Elearning_app.categorie'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='courseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='Elearning_app.course'),
        ),
    ]