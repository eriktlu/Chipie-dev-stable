# Generated by Django 4.0.2 on 2022-05-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crash', '0005_crashbets_stop_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crashbets',
            name='win',
            field=models.BooleanField(default=None, null=True),
        ),
    ]