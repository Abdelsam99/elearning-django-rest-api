"""
URL configuration for Elearning_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import AnswerNoticeListView, CategorieListView, CourseCategoryView, CourseListView, LessonCourseView, LessonListView, NoticeListView

urlpatterns = [
    path('elearning/categorie/list/', CategorieListView.as_view()),
    path('elearning/course/list/', CourseListView.as_view()),
    path('elearning/lesson/list/', LessonListView.as_view()),
    path('elearning/courseCategorie/<int:category_id>/', CourseCategoryView.as_view()),
    path('elearning/LessonCourse/<int:course_id>/', LessonCourseView.as_view()),
    path('elearning/notice/list/', NoticeListView.as_view()),
    path('elearning/answerNotice/list/', AnswerNoticeListView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
