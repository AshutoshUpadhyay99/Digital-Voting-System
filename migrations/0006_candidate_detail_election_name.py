# Generated by Django 4.1.7 on 2023-03-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0005_rename_name_voter_register_voter_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate_detail',
            name='election_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]