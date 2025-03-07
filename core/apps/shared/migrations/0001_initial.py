# Generated by Django 5.1.3 on 2025-03-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='media/', verbose_name='file')),
            ],
            options={
                'verbose_name': 'MediaModel',
                'verbose_name_plural': 'MediaModels',
                'db_table': 'media',
            },
        ),
    ]
