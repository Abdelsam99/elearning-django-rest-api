# Generated by Django 4.2 on 2023-04-12 11:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Elearning_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('filePresentation', models.ImageField(blank=True, null=True, upload_to='courseImage/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning_app.categorie')),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('video', models.FileField(upload_to='lessonvideos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])])),
                ('duration', models.DurationField(blank=True, null=True)),
                ('filePdf', models.FileField(blank=True, null=True, upload_to='lessonFile/')),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning_app.categorie')),
                ('courseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning_app.course')),
            ],
            options={
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.TextField(blank=True, null=True)),
                ('note', models.CharField(max_length=255)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elearning_app.course')),
            ],
            options={
                'verbose_name_plural': 'Notices',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.IntegerField()),
                ('type_profil', models.CharField(choices=[('Etudiant', 'Etudiant'), ('Teacher', 'Teacher')], default='Etudiant', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, to='Elearning_app.profile'),
        ),
    ]
