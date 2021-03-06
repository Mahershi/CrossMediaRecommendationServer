# Generated by Django 4.0.3 on 2022-03-23 08:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0024_brokenlinkmodel_completed_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='backdrop_path',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='imdb_id',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='language',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='overview',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='popularity',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='poster_path',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='release_date',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='runtime',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='spoken_languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='status',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='last_air_date',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='no_episodes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='no_seasons',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='original_language',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='overview',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='poster_path',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='spoken_languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=5), size=None),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='status',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
