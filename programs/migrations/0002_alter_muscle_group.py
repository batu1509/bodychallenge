# Generated by Django 4.0.4 on 2022-09-24 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muscle',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='programs.musclegroup'),
        ),
    ]