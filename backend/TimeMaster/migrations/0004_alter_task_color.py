# Generated by Django 3.2.23 on 2024-01-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeMaster', '0003_task_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='color',
            field=models.CharField(max_length=200),
        ),
    ]