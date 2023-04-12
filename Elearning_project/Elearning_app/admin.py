from django.contrib import admin
from .models import *

# Register your models here.
# class ProducAdmin(admin.ModelAdmin):
#     list_display=('name','content','price','timestamp','completed')

admin.site.register(Profile)
admin.site.register(Categorie)
admin.site.register(Course)
admin.site.register(Lesson)