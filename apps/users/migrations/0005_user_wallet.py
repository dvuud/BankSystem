# Generated by Django 5.0.4 on 2024-04-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wallet',
            field=models.PositiveIntegerField(default=0, verbose_name='Кошелек'),
        ),
    ]