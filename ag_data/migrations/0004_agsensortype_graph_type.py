# Generated by Django 2.2.11 on 2020-04-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ag_data', '0003_errorlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='agsensortype',
            name='graph_type',
            field=models.CharField(choices=[('graph', 'Graph'), ('map', 'Map'), ('gauge', 'Gauge')], default='graph', max_length=20),
        ),
    ]
