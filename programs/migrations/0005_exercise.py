# Generated by Django 4.0.4 on 2022-09-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_equipment_exercisemechanic_exercisetype_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='exercise_photos/%Y/%m/')),
                ('video', models.CharField(max_length=255, null=True)),
                ('primaryTargetMuscles', models.ManyToManyField(related_name='primaryTargetMuscles', to='programs.muscle')),
                ('secondaryTargetMuscles', models.ManyToManyField(related_name='secondaryTargetMuscles', to='programs.muscle')),
            ],
        ),
    ]