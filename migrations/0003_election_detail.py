# Generated by Django 4.1.7 on 2023-03-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0002_master_table_voter_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='election_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_name', models.CharField(default=None, max_length=100, null=True)),
                ('election_category', models.CharField(default=None, max_length=100, null=True)),
                ('election_date', models.CharField(default=None, max_length=100, null=True)),
                ('election_commission', models.CharField(default=None, max_length=100, null=True)),
                ('state', models.CharField(default=None, max_length=100, null=True)),
            ],
            options={
                'db_table': 'election_detail',
            },
        ),
    ]
