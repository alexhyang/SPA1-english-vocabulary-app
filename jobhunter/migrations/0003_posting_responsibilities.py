# Generated by Django 3.2.4 on 2021-07-02 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobhunter', '0002_auto_20210701_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='responsibilities',
            field=models.TextField(default=''),
        ),
    ]
