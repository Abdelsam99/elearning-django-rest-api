from django.shortcuts import render
from .models import AnswerNotice, Categorie, Course, Lesson, Notice
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnswerNoticeSerializer, CategorieSerializer, CourseSerializer, LessonSerializer, NoticeSerializer
# Create your views here.
class CategorieListView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class=CategorieSerializer
    """Cette methode est une surcharge"""
    def get_queryset(self):
        return super().get_queryset()
    
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class=CourseSerializer
    """Cette methode est une surcharge"""
    def get_queryset(self):
        return super().get_queryset()
    
class LessonListView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class=LessonSerializer
    """Cette methode est une surcharge"""
    def get_queryset(self):
        return super().get_queryset()
    
class NoticeListView(generics.ListCreateAPIView):
    queryset = Notice.objects.all() 
    serializer_class=NoticeSerializer
    """Cette methode est une surcharge"""
    def get_queryset(self):
        return super().get_queryset()

class AnswerNoticeListView(generics.ListCreateAPIView):
    queryset = AnswerNotice.objects.all()
    serializer_class=AnswerNoticeSerializer
    """Cette methode est une surcharge"""
    def get_queryset(self):
        return super().get_queryset()
    
class CourseCategoryView(APIView):
    def get(self, request, category_id, *args, **kwargs):
        categories = Course.objects.filter(categoryId=category_id)
        serializer=CourseSerializer(categories, many=True)
        return Response(serializer.data)

class LessonCourseView(APIView):
    def get(self, request, course_id, *args, **kwargs):
        course = Lesson.objects.filter(courseID=course_id)
        serializer=LessonSerializer(course, many=True)
        return Response(serializer.data)
    
class CategorieDetailView(generics.RetrieveAPIView):
    queryset = Categorie.objects.all()
    serializer_class=CategorieSerializer
# class CourseCategoryView(generics.RetrieveAPIView):
#     serializer_class=CourseSerializer
#     queryset = Course.objects.all()
#     lookup_field='categoryId'
    
#     def get_object(self):
#         category_id= self.kwargs.get('category_id')
#         course=self.get_queryset().filter(categoryId=category_id)
#         return course


    """Cette classe est pour la modification d'une Categorie"""
class CategorieUpdateView(generics.UpdateAPIView):
    queryset = Categorie.objects.all()
    serializer_class=CategorieSerializer
    
    """Cette classe est pour la suppression d'une Categorie"""
class CategorieDeleteView(generics.DestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class=CategorieSerializer