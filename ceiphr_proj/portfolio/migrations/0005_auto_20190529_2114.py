# Generated by Django 2.2.1 on 2019-05-30 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20190529_2113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-active', '-end_date']},
        ),
    ]
