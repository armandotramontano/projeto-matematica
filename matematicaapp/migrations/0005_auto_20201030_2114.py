# Generated by Django 2.2.16 on 2020-10-31 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matematicaapp', '0004_questao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='enunciado',
            field=models.TextField(max_length=20),
        ),
    ]
