# Generated by Django 2.2.7 on 2020-04-18 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0005_auto_20200418_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access_instance',
            name='accessed_camera',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='console.Camera'),
        ),
    ]