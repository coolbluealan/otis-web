# Generated by Django 4.0.7 on 2022-08-23 03:19

import dashboard.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0073_achievement_always_show_image_alter_achievement_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='content',
            field=models.FileField(help_text='Upload your write-ups as PDF, TeX, TXT, PNG, or JPG. At most one file.', upload_to=dashboard.models.content_file_name, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'tex', 'png', 'jpg'])], verbose_name='Your submission'),
        ),
    ]