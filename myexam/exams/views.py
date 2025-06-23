from django.shortcuts import render
from .models import Exam

def tbexam_list(request):
    exams = Exam.objects.filter(is_public=True).order_by('exam_date')
    context = {
        'exams': exams,
    }
    return render(request, 'exams/tbexam_list.html', context)