from django.db import models

# Create your models here.

class UserForm(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    term = models.BooleanField()

    def __str__(self):
        return self.nome


