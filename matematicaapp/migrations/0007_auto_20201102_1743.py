# Generated by Django 2.2.16 on 2020-11-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matematicaapp', '0006_questao_figura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='enunciado',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='questao',
            name='figura',
            field=models.FileField(default='12', upload_to='assets/questoes5ano'),
        ),
    ]