# Generated by Django 3.1.3 on 2021-09-02 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20210902_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
