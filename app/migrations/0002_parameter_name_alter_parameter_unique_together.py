# Generated by Django 5.0.3 on 2024-03-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='name',
            field=models.CharField(default='teste', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='parameter',
            unique_together={('name', 'path')},
        ),
    ]
