# Generated by Django 4.2.2 on 2024-07-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='floor',
            name='busy_place',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='floor',
            name='empty_place',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
