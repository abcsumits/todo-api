# Generated by Django 4.2.3 on 2023-12-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_item',
            name='status',
            field=models.CharField(default='OPEN', max_length=100),
        ),
        migrations.AddField(
            model_name='todo_item',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='todo_item',
            name='tag',
            field=models.CharField(default='', max_length=100),
        ),
    ]
