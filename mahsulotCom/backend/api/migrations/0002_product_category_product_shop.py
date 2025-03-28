# Generated by Django 4.2.2 on 2024-03-31 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='api.shop'),
            preserve_default=False,
        ),
    ]
