# Generated by Django 4.1.7 on 2023-03-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0008_rename_add_vote_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate_detail',
            name='Type_of_Election',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
