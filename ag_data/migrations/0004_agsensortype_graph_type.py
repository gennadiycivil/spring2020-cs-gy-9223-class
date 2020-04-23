# Generated by Django 2.2.11 on 2020-04-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ag_data', '0003_errorlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='agsensortype',
            name='graph_type',
            field=models.CharField(choices=[('time_series', 'Time-series'), ('map', 'Map'), ('single_value', 'Single-value')], default='time_series', max_length=20),
        ),
    ]
