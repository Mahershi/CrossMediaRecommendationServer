# Generated by Django 4.0.3 on 2022-03-17 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0011_remove_brokenlinkmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='tagline',
            field=models.TextField(default=''),
        ),
    ]
