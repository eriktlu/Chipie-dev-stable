# Generated by Django 4.0.2 on 2022-05-12 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('round_number', models.IntegerField(default=0, unique=True)),
                ('round_start_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CrashPublicSeeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_seed', models.CharField(max_length=32)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CrashServerSeeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_seed', models.CharField(max_length=64)),
                ('hashed_server_seed', models.CharField(max_length=64)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CrashBets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('win', models.BooleanField(default=False)),
                ('bet_time', models.DateTimeField(auto_now_add=True)),
                ('crash_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crash_round', to='crash.crash')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crash_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='crash',
            name='used_public_seed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crash_used_public_seed', to='crash.crashpublicseeds'),
        ),
        migrations.AddField(
            model_name='crash',
            name='used_server_seed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crash_used_server_seed', to='crash.crashserverseeds'),
        ),
    ]
