# Generated by Django 4.0.4 on 2022-05-23 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pplelo', '0008_statistic_win'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_statistic', to='pplelo.match'),
        ),
    ]
