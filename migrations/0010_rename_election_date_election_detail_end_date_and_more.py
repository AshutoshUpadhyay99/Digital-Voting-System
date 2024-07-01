# Generated by Django 4.1.7 on 2023-03-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0009_candidate_detail_type_of_election'),
    ]

    operations = [
        migrations.RenameField(
            model_name='election_detail',
            old_name='election_date',
            new_name='end_date',
        ),
        migrations.RemoveField(
            model_name='candidate_detail',
            name='Type_of_Election',
        ),
        migrations.AddField(
            model_name='election_detail',
            name='start_date',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]