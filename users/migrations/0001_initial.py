# Generated by Django 3.2.11 on 2022-01-11 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('nome', models.CharField(max_length=60)),
                ('senha', models.CharField(max_length=60)),
                ('cod_user', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
