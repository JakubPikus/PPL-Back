# Generated by Django 4.0.4 on 2022-05-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pplelo', '0013_statistic_nickname_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='win',
            field=models.CharField(max_length=2),
        ),
    ]
