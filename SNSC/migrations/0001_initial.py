# Generated by Django 2.1.3 on 2019-02-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SNSC_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassRoomID', models.CharField(max_length=3)),
                ('NumofStudent', models.CharField(max_length=3)),
            ],
        ),
    ]
