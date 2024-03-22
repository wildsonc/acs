# Generated by Django 5.0.3 on 2024-03-22 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'models',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('writable', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'parameters',
                'ordering': ['path'],
            },
        ),
        migrations.CreateModel(
            name='CPE',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('sn', models.CharField(db_index=True, max_length=12)),
                ('parameters', models.JSONField(default=dict)),
                ('manufacturer', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_seen', models.DateTimeField(null=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cpes', to='app.model')),
            ],
            options={
                'db_table': 'cpes',
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='model',
            name='parameters',
            field=models.ManyToManyField(related_name='models', to='app.parameter'),
        ),
    ]
