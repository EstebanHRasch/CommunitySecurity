# Generated by Django 2.2.7 on 2020-04-18 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0004_remove_footage_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='access_instance',
            name='accessed_camera_location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='access_instance',
            name='accessed_footage',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='console.Footage'),
        ),
        migrations.AddField(
            model_name='access_instance',
            name='accessed_footage_time',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
