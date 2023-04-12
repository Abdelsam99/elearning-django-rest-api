from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from moviepy.video.io.VideoFileClip import VideoFileClip
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    tel=models.IntegerField()
    student="Etudiant"
    teacher="Teacher"
    TYPE_USER=[
        (student, "Etudiant"),
        (teacher,"Teacher"),
    ]
    type_profil=models.CharField(max_length=20, choices=TYPE_USER, default=student)

    class Meta:
        verbose_name_plural = ("Profiles")
    def __str__(self):
        return self.user.username
    
class Categorie(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs ):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)


class Course(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    filePresentation=models.ImageField(upload_to="courseImage/", null=True, blank=True)
    student = models.ManyToManyField('Profile', blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categoryId=models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs ):
        if self.slug:
            self.slug=slugify(self.title)
        super().save(*args, **kwargs)
    
class Lesson(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(null=True, blank=True)
    video=models.FileField(upload_to='lessonvideos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])])
    duration=models.DurationField(null=True, blank=True)
    filePdf=models.FileField(upload_to="lessonFile/", null=True, blank=True)
    courseID=models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ("Lessons")

    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs ):
    #     self.slug=slugify(self.name)
    #     super().save(*args, **kwargs)

# @receiver(pre_save, sender=Lesson)
# def calculate_duration(sender, instance, **kwargs):
#     if not instance.duration:
#         with VideoFileClip(instance.video.path) as video:
#             duration = int(video.duration // 60)
#             instance.duration=duration


class Notice(models.Model):
    opinion=models.TextField(null=True, blank=True)
    note=models.CharField(max_length=255)
    autor=models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ("Notices")

    def __str__(self):
        return self.opinion