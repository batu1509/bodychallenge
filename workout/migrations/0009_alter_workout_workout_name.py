# Generated by Django 3.2 on 2022-04-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plannerapp', '0008_alter_workout_workout_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
