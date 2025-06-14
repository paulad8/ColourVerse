# Generated by Django 5.0.6 on 2024-11-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("artworks", "0007_artist_movement"),
    ]

    operations = [
        migrations.CreateModel(
            name="Medium",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="artwork",
            name="medium",
        ),
        migrations.AddField(
            model_name="artwork",
            name="medium",
            field=models.ManyToManyField(to="artworks.medium"),
        ),
    ]
