# Generated by Django 4.0.4 on 2022-06-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0012_alter_workout_total_rounds'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='demo_src',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
