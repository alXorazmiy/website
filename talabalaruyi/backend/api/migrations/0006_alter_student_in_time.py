# Generated by Django 4.2.2 on 2024-07-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_student_out_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='in_time',
            field=models.DateTimeField(),
        ),
    ]
