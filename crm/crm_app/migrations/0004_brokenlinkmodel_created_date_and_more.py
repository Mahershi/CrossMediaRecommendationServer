# Generated by Django 4.0.3 on 2022-03-15 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0003_inaccuraterecommodel_inaccuratedatamodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brokenlinkmodel',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='inaccuratedatamodel',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='inaccuraterecommodel',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
