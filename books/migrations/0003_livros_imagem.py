# Generated by Django 3.2.11 on 2022-02-09 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_cod_user_livros_cod_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='imagem',
            field=models.ImageField(null=True, upload_to='BD_imagens/'),
        ),
    ]
