# Generated by Django 5.1.2 on 2024-11-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_paciente_grau_parentesco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='nome_responsavel',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefone_responsavel',
            field=models.CharField(max_length=20),
        ),
    ]
