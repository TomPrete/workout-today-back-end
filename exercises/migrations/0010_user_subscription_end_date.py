# Generated by Django 4.0.4 on 2022-11-27 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0009_user_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscription_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
