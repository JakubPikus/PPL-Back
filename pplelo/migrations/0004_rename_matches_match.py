# Generated by Django 4.0.4 on 2022-05-17 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pplelo', '0003_matches'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Matches',
            new_name='Match',
        ),
    ]