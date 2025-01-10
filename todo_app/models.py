from django.db import models

# Create your models here.
class Todo(models.Model):
    title= models.CharField(max_length=200)

    def __str__ (self):
        return self.title

#When there is change in models.py
#python manage.py makemigrations
#python manage.py migrate

