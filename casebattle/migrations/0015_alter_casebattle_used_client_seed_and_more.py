# Generated by Django 4.0.2 on 2022-05-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casebattle', '0014_alter_casebattle_battle_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casebattle',
            name='used_client_seed',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='casebattle',
            name='used_hashed_server_seed',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='casebattle',
            name='used_server_seed',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]