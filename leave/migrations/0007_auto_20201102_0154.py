# Generated by Django 3.1.2 on 2020-11-01 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0006_auto_20180319_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='prefix',
        ),
        migrations.RemoveField(
            model_name='application',
            name='suffix',
        ),
    ]