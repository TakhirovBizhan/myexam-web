from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'exam_date', 'is_public', 'created_at')
    search_fields = ('title', 'users__email')  
    date_hierarchy = 'exam_date'  
    list_filter = ('is_public', 'created_at')  
    filter_horizontal = ('users',)