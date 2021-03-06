# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-21 10:52
from __future__ import unicode_literals

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
            name='AcademyGroup',
            fields=[
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, choices=[('m1', '중1'), ('m2', '중2'), ('m3', '중3'), ('h1', '고1'), ('h2', '고2'), ('h3', '고3'), ('df', '없음')], max_length=2)),
                ('academy_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.AcademyGroup')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolGroup',
            fields=[
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='school_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.SchoolGroup'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
