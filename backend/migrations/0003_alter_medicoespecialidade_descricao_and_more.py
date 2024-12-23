# Generated by Django 5.1.2 on 2024-11-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_profile_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicoespecialidade',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='alergias',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='alteracoes_humor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cirurgias',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='comportamento_social',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='condicoes_cognitivas',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='doencas_cronicas',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='exames',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='historico_internacoes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='medicamentos',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='vacinas',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
