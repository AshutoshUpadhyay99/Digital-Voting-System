# Generated by Django 4.1.7 on 2023-03-04 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0007_add_vote'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_vote',
            new_name='vote',
        ),
    ]
