# Generated by Django 4.0.2 on 2022-05-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casebattle', '0015_alter_casebattle_used_client_seed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casebattle',
            name='battle_result_coins',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10),
        ),
    ]
