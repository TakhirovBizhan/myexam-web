from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model): # забыл добавить инициалы
    title = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True) 
    exam_date = models.DateField()  
    image = models.ImageField(upload_to='exam_images/') 
    users = models.ManyToManyField(User, related_name='exams')  
    is_public = models.BooleanField(default=False) 

    def __str__(self):
        return self.title