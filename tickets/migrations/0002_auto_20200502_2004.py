# Generated by Django 3.0.5 on 2020-05-02 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='issue_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='ticket_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='ticket_title',
            new_name='title',
        ),
    ]
