# Generated by Django 4.1.7 on 2023-10-25 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0016_remove_vote_manipulation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='Block',
        ),
    ]