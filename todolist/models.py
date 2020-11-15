from django.db import models

# Create your models here.

class Todolist(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    duration = models.DurationField(default='00:00:00')

    def __str__(self):
        return self.title


    