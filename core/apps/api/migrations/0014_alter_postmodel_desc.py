# Generated by Django 5.1.3 on 2025-03-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_postmodel_desc_alter_postmodel_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='desc',
            field=models.CharField(max_length=1000, verbose_name='desc'),
        ),
    ]
