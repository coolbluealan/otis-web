# Generated by Django 3.2.9 on 2021-11-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0015_alter_market_alpha'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='show_answer',
            field=models.BooleanField(default=False),
        ),
    ]