# Generated by Django 4.0.2 on 2022-04-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0004_alter_depositeditems_asset_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='depositeditems',
            name='buyer_trade_link',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]