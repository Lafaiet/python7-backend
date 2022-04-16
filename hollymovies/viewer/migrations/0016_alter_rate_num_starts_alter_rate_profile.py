# Generated by Django 4.0.2 on 2022-04-16 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0015_profile_age_profile_alergic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='num_starts',
            field=models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='rate',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='viewer.profile'),
        ),
    ]
