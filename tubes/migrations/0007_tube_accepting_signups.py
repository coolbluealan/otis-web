# Generated by Django 4.2.7 on 2023-12-04 03:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tubes", "0006_remove_joinrecord_success_remove_tube_join_url_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tube",
            name="accepting_signups",
            field=models.BooleanField(
                default=True, help_text="Whether to allow people to join"
            ),
        ),
    ]
