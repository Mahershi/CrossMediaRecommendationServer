# Generated by Django 4.0.3 on 2022-03-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0010_rename_movie_id1_moviemovierecommodel_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviemovierecommodel',
            name='movie',
        ),
        migrations.AddField(
            model_name='moviemovierecommodel',
            name='movie_id1',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='moviemovierecommodel',
            name='movie_id2',
            field=models.CharField(default='', max_length=15),
        ),
    ]