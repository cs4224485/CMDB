# Generated by Django 2.1.1 on 2019-07-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_disk_manufactory'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='token',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='token'),
        ),
    ]
