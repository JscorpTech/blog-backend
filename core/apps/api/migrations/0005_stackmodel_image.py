# Generated by Django 5.1.3 on 2025-03-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_stackcategorymodel_stackmodel_delete_skilmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='stackmodel',
            name='image',
            field=models.ImageField(default=1, upload_to='stack/', verbose_name='image'),
            preserve_default=False,
        ),
    ]
