# Generated by Django 4.0.4 on 2022-05-19 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pplelo', '0006_remove_match_kak1_remove_match_kak10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_id',
            field=models.CharField(max_length=100),
        ),
    ]