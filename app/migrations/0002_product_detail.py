# Generated by Django 3.0.7 on 2020-06-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]