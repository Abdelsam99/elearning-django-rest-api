from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='autor', read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'user_name', 'title', 'slug', 'description',
                  'filePresentation', 'student', 'autor', 'categoryId')


class CategorieSerializer(serializers.ModelSerializer):
    categories = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Categorie
        fields = ('id', 'name', 'slug', 'categories')


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'slug', 'video',
                  'duration', 'filePdf', 'courseID',)


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = ('id', 'opinion', 'note', 'course', 'autor', 'date',)


class AnswerNoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerNotice
        fields = ('id', 'answer', 'notice', 'course', 'autor', 'date',)
