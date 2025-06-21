from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'marks', 'teacher')  
    search_fields = ('name', 'subject')  
    list_filter = ('subject', 'teacher') 

