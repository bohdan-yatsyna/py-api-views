# Generated by Django 4.1 on 2023-06-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0003_rename_cinemahal_cinemahall"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="first_name",
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name="actor",
            name="last_name",
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name="cinemahall",
            name="name",
            field=models.CharField(max_length=65, unique=True),
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(max_length=65, unique=True),
        ),
    ]
