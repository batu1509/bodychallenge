# Generated by Django 4.0.4 on 2022-10-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0008_remove_routine_level_routine_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutexercise',
            name='linkedExercise',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='workoutexercise',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]