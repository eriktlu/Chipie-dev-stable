# Generated by Django 4.0.2 on 2022-05-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crash', '0007_alter_crashbets_stop_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crashbets',
            name='stop_point',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
