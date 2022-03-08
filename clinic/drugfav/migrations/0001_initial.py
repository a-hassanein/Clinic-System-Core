# Generated by Django 3.2.10 on 2022-03-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavDrugs',
            fields=[
                ('drugid', models.AutoField(primary_key=True, serialize=False)),
                ('favname', models.CharField(max_length=100)),
                ('favdose', models.CharField(max_length=100)),
                ('favdosageform', models.CharField(max_length=50)),
                ('favfrequency', models.CharField(max_length=100)),
                ('favnoofdays', models.IntegerField()),
                ('favduration', models.CharField(max_length=50)),
                ('favinstructions', models.TextField()),
            ],
        ),
    ]