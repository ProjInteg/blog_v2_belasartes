# Generated by Django 4.0.4 on 2022-05-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Associado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_associado', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=30)),
                ('telefone', models.CharField(blank=True, max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
