# Generated by Django 2.0b1 on 2017-11-06 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_auto_20171106_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='licenserequest',
            name='team',
            field=models.ForeignKey(help_text='The team whose license pool is drawn from. Must be a team that the user is a member of.', null=True, on_delete=django.db.models.deletion.CASCADE, to='marketplace.Team'),
        ),
    ]
