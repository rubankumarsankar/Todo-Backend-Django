from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    
    title = models.CharField(max_length=200)
    due_date = models.CharField(max_length=50)
    due_time = models.CharField(max_length=50)
    status = models.CharField( default=0)

    def __str__(self):
        return f"{self.title} - {self.status}"

