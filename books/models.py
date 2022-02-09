from audioop import reverse
from django.db import models
from users.models import Users
from django.urls import reverse

#from django.contrib.auth.models import user
# Create your models here.


class Livros(models.Model):
    titulo = models.CharField(max_length=70, blank=False,  null=False)
    editora = models.CharField(max_length=70, blank=True,  null=True)
    autor = models.CharField(max_length=255, blank=True,  null=True)
    resenha = models.TextField(blank=True,  null=True)
    cod_book = models.AutoField(primary_key=True) 
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='media/',blank=True, null=True)
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('books:list')

        