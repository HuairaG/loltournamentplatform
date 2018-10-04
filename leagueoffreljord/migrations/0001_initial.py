# Generated by Django 2.1 on 2018-09-15 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import leagueoffreljord.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nickname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=48)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('dni', models.PositiveIntegerField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to=leagueoffreljord.usermodels.upload_location)),
                ('league', models.CharField(max_length=80)),
                ('nickname', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='leagueoffreljord.Nickname')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]