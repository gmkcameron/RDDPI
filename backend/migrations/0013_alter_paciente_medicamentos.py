# Generated by Django 5.1.2 on 2024-11-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_remove_prontuario_medicamento_aplicado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='medicamentos',
            field=models.TextField(blank=True, null=True),
        ),
    ]
