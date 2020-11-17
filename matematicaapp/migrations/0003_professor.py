# Generated by Django 2.2.16 on 2020-10-22 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('matematicaapp', '0002_auto_20201022_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('data_de_nascimento', models.CharField(max_length=10)),
                ('formacao', models.CharField(choices=[('1', 'Curso Normal'), ('2', 'Graduação em Matemática'), ('3', 'Graduação em Pedagogia')], default='2', max_length=20)),
                ('instituicao', models.TextField()),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('foto', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]