# Generated by Django 3.1.3 on 2021-09-01 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210901_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='highest_bidder',
            field=models.ForeignKey(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_id', to='backend.users'), on_delete=django.db.models.deletion.CASCADE, related_name='highest_bidder', to='backend.users'),
        ),
    ]
