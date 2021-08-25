from django.db import models

# Create your models here.
class Todo(models.Model):

    choices_priority = [
        ('Urgent', 'Urgent'),
        ('Medium', 'Medium'),
        ('Later', 'Later'),
    ]

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=6, choices=choices_priority)
    created_at = models.DateTimeField(auto_now=True)
   
    def __str__(self) -> str:
        return self.title