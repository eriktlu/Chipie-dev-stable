# Generated by Django 4.0.2 on 2022-04-05 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0008_depositeditems_buyer_item_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositeditems',
            name='buyer_item_count',
            field=models.IntegerField(default=0),
        ),
    ]
