# Generated by Django 3.2.11 on 2022-02-10 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_livros_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
    ]
