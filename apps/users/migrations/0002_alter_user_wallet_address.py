# Generated by Django 5.0.4 on 2024-04-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wallet_address',
            field=models.CharField(blank=True, max_length=12, verbose_name='ID кошелька'),
        ),
    ]
