# Generated by Django 5.1.3 on 2025-03-07 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_experiencemodel_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencemodel',
            name='role',
            field=models.CharField(default=1, max_length=255, verbose_name='role'),
            preserve_default=False,
        ),
    ]
