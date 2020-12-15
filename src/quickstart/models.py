from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.lastname
