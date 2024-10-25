# Generated by Django 4.2.15 on 2024-09-19 16:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("car_specifications", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shape",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("shape_name", models.CharField(max_length=60)),
            ],
            options={
                "db_table": "shape",
            },
        ),
        migrations.CreateModel(
            name="CarShape",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("shape_name", models.CharField(blank=True, max_length=60, null=True)),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="car_specifications.car",
                    ),
                ),
                (
                    "shape",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="shape.shape",
                    ),
                ),
            ],
            options={
                "db_table": "car_shape",
            },
        ),
    ]
