# Generated by Django 3.2.4 on 2021-07-03 18:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('emp_num', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_text', models.CharField(max_length=100)),
                ('detail_text', models.CharField(max_length=100)),
                ('record_comment', models.CharField(default=None, max_length=100)),
                ('record_time', models.DateField(verbose_name=datetime.datetime(2021, 7, 4, 2, 53, 44, 993764))),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.depart')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(auto_now_add=True)),
                ('action', models.CharField(max_length=30)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.record')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]