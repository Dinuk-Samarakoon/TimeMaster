# Generated by Django 3.2.23 on 2024-01-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeMaster', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='color',
            field=models.CharField(default='', max_length=200),
        ),
    ]
