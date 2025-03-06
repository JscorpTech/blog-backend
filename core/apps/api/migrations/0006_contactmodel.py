# Generated by Django 5.1.3 on 2025-03-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_stackmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('phone', models.CharField(max_length=255, verbose_name='phone')),
            ],
            options={
                'verbose_name': 'ContactModel',
                'verbose_name_plural': 'ContactModels',
                'db_table': 'contact',
            },
        ),
    ]
