# Generated by Django 4.2.1 on 2023-05-29 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0005_rename_artist_pk_record_artist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="artist",
            field=models.CharField(max_length=125, unique=True),
        ),
        migrations.AlterField(
            model_name="record",
            name="album",
            field=models.CharField(max_length=125, unique=True),
        ),
    ]
