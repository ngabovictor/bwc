# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-24 18:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(help_text='Add images with same resolutions', upload_to='media/home/carousel')),
                ('title', models.CharField(help_text='Add an image title', max_length=50)),
                ('caption', models.TextField(help_text='Add an image more description')),
            ],
        ),
        migrations.CreateModel(
            name='mailbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date', models.DateField(default=datetime.datetime(2017, 9, 24, 18, 45, 45, 282096))),
                ('classifications', models.CharField(choices=[('Read', 'Read'), ('Unread', 'Unread')], default='Unread', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Add the title', max_length=50)),
                ('image', models.FileField(help_text='Add a thumbnail of the work', upload_to='media/home/programs')),
                ('caption', models.TextField(help_text='Add a short caption')),
                ('description', models.TextField(help_text='Add a full description.')),
            ],
        ),
        migrations.CreateModel(
            name='publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(help_text='Add a thumbnail of the publication', upload_to='media/home/publications')),
                ('title', models.CharField(help_text='Add the title', max_length=50)),
                ('caption', models.TextField(help_text='Add the description')),
                ('author', models.CharField(help_text="Add the author's name", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='registered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(help_text='Add names', max_length=50)),
                ('description', models.TextField(help_text='Add a full description.')),
                ('date', models.DateField(default=datetime.datetime(2017, 9, 24, 18, 45, 45, 281032))),
                ('paid', models.CharField(help_text='Add the amount paid in RWF.', max_length=50)),
                ('duration', models.CharField(help_text='Duration in months', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Add the title', max_length=50)),
                ('image', models.FileField(help_text='Add a thumbnail of the work', upload_to='media/home/trainings')),
                ('caption', models.TextField(help_text='Add a short caption')),
                ('description', models.TextField(help_text='Add a full description.')),
                ('price', models.CharField(help_text="Add the training's price in RWF.", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Add the title', max_length=50)),
                ('image', models.FileField(help_text='Add a thumbnail of the work', upload_to='media/home/activities')),
                ('icon', models.CharField(help_text='Add the icon, please make sure you write correctly, otherwise the icon will be missing. visit http://fontawesome.io for accurate names.', max_length=50)),
                ('caption', models.TextField(help_text='Add a short caption')),
                ('date', models.DateField(default=datetime.datetime(2017, 9, 24, 18, 45, 45, 278506))),
                ('description', models.TextField(help_text='Add a full description.')),
            ],
        ),
        migrations.CreateModel(
            name='work_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Add the title', max_length=50)),
                ('description', models.TextField(help_text='Add the description')),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='category',
            field=models.ForeignKey(help_text='Choose category for the work.', on_delete=django.db.models.deletion.CASCADE, to='bwc.work_category'),
        ),
        migrations.AddField(
            model_name='registered',
            name='training',
            field=models.ForeignKey(help_text='training registered.', on_delete=django.db.models.deletion.CASCADE, to='bwc.training'),
        ),
    ]