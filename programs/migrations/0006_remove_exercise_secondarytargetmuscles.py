# Generated by Django 4.0.4 on 2022-11-03 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_alter_exercise_intervalonly_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='secondaryTargetMuscles',
        ),
    ]
