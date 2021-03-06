# Generated by Django 3.0.5 on 2020-05-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20200502_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('OPENED', 'Opened'), ('INPROG', 'In progress'), ('SOLVED', 'Solved')], default='OPENED', max_length=6),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('BUG', 'Bug'), ('FEATURE', 'Feature')], default='BUG', max_length=7),
        ),
    ]
