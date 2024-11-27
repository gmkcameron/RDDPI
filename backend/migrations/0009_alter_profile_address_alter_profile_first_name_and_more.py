# Generated by Django 5.1.2 on 2024-11-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_profile_estado_civil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, default='Não informado', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genero',
            field=models.CharField(blank=True, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outro', 'Outro')], default='Outro', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, default='Sem telefone cadastrado', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rg',
            field=models.CharField(blank=True, default='Sem RG cadastrado', max_length=20, null=True, unique=True),
        ),
    ]