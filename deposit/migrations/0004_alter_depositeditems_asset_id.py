# Generated by Django 4.0.2 on 2022-04-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0003_depositeditems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositeditems',
            name='asset_id',
            field=models.CharField(max_length=128),
        ),
    ]
