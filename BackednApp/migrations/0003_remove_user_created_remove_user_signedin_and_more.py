# Generated by Django 4.0.4 on 2022-11-23 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackednApp', '0002_remove_user_id_alter_user_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='signedIn',
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(to='BackednApp.user'),
        ),
        migrations.AddField(
            model_name='user',
            name='rankPoints',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='WaterConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waterSourceName', models.CharField(max_length=15)),
                ('waterConsumptionPerHour', models.IntegerField()),
                ('unit', models.CharField(max_length=5)),
                ('hoursOfUsage', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackednApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rankName', models.CharField(max_length=10)),
                ('minRankPoints', models.IntegerField()),
                ('maxRankPoints', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackednApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='HeatingConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatureInYourHoushold', models.IntegerField()),
                ('electricityConsumptionPerHour', models.IntegerField()),
                ('unit', models.CharField(max_length=5)),
                ('hoursOfUsage', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackednApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='ElectrictyConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricitySourceName', models.CharField(max_length=15)),
                ('electricityConsumptionPerHour', models.IntegerField()),
                ('unit', models.CharField(max_length=5)),
                ('hoursOfUsage', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackednApp.user')),
            ],
        ),
    ]
