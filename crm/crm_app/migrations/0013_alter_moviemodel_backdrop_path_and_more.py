# Generated by Django 4.0.3 on 2022-03-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0012_alter_moviemodel_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='backdrop_path',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='poster_path',
            field=models.CharField(max_length=50),
        ),
    ]