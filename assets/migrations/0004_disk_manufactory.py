# Generated by Django 2.1.1 on 2019-07-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20190702_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='disk',
            name='manufactory',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='制造商'),
        ),
    ]
