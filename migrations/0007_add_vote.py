# Generated by Django 4.1.7 on 2023-03-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0006_candidate_detail_election_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.CharField(default=None, max_length=100, null=True)),
                ('election_id', models.CharField(default=None, max_length=100, null=True)),
                ('candidate_id', models.CharField(default=None, max_length=100, null=True)),
                ('candidate_name', models.CharField(default=None, max_length=100, null=True)),
                ('political_party', models.CharField(default=None, max_length=100, null=True)),
                ('election_name', models.CharField(default=None, max_length=100, null=True)),
            ],
            options={
                'db_table': 'add_vote',
            },
        ),
    ]
