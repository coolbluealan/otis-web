# Generated by Django 5.0.7 on 2024-07-28 07:16

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import opal.models


class Migration(migrations.Migration):
    dependencies = [
        ("opal", "0003_alter_opalhunt_author_draft_deadline_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="OpalPuzzle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(help_text="Slug for the puzzle")),
                (
                    "title",
                    models.CharField(help_text="Name of the puzzle", max_length=128),
                ),
                (
                    "answer",
                    models.CharField(
                        help_text="Answer to the puzzle, as displayed", max_length=128
                    ),
                ),
                (
                    "num_to_unlock",
                    models.PositiveSmallIntegerField(
                        default=0,
                        help_text="Number of solves needed before this OPAL puzzle is unlocked",
                    ),
                ),
                (
                    "content",
                    models.FileField(
                        blank=True,
                        help_text="PDF of the puzzle you are uploading",
                        null=True,
                        upload_to=opal.models.puzzle_file_name,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["pdf"]
                            )
                        ],
                        verbose_name="Puzzle file",
                    ),
                ),
                (
                    "hunt",
                    models.ForeignKey(
                        help_text="The hunt this puzzle belongs to",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="opal.opalhunt",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OpalAttempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_correct",
                    models.BooleanField(
                        help_text="Whether the attempt was judged correct"
                    ),
                ),
                ("guess", models.CharField(help_text="The guess", max_length=128)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user making the attempt",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "puzzle",
                    models.ForeignKey(
                        help_text="The puzzle being attempted",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="opal.opalpuzzle",
                    ),
                ),
            ],
        ),
    ]