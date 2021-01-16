from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    shelf = models.ForeignKey(Shelf,default=None,on_delete=models.SET_NULL)

    def assign_to(self,shelf):
        self.shelf = shelf

    def get_shelf(self):
        return self.shelf

    def __str__(self):
        return self.name

class Shelf(models.Model):
    name = models.CharField(max_length=200, null=True)

    def get_books(self):
        
        return Book.objects.filter(self.name)

    def __str__(self):
        return self.name