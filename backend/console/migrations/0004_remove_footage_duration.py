# Generated by Django 2.2.7 on 2020-04-18 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0003_auto_20200418_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footage',
            name='duration',
        ),
    ]
