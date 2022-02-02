from django.db import models
# Create your models here.

class Users(models.Model):
    nome = models.CharField(max_length=60, null=False)
    senha = models.CharField(max_length=60, null=False)
    cod_user = models.AutoField(primary_key=True)
