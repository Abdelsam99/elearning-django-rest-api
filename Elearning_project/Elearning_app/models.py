from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from moviepy.video.io.VideoFileClip import VideoFileClip
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    tel=models.IntegerField()

    class Meta:
        verbose_name_plural = ("Students")
    def __str__(self):
        return self.name
    
class Categorie(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name


class Teacher(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    tel=models.IntegerField()

    class Meta:
        verbose_name_plural = ("Teachers")
    def __str__(self):
        return self.name

class Course(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to="courseImage/")
    student = models.ManyToManyField('Student', blank=True)
    autor=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    categoryId=models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.title

class Lesson(models.Model):
    name=models.CharField(max_length=255)
    video=models.FileField(upload_to="courseVideo/")
    duration=models.DurationField(null=True, blank=True)
    file=models.FileField(upload_to="courseFile/")
    autor=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    categoryId=models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ("Lessons")

    def __str__(self):
        return self.name
    
@receiver(pre_save, sender=Lesson)
def calculate_duration(sender, instance, **kwargs):
    if not instance.duration:
        with VideoFileClip(instance.video) as video:
            duration = int(video.duration // 60)
            instance.duration=duration

class Notice(models.Model):
    opinion=models.TextField(null=True, blank=True)
    note=models.CharField(max_length=255)
    autor=models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ("Notices")

    def __str__(self):
        return self.opinion