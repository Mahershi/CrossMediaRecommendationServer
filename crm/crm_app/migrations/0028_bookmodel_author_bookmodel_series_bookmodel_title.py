# Generated by Django 4.0.3 on 2022-03-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0027_rename_amazon_link_bookmodel_amazon_redirect_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='series',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]