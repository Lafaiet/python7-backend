# Generated by Django 4.0.2 on 2022-04-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0014_profile_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='alergic',
            field=models.BooleanField(default=False),
        ),
    ]