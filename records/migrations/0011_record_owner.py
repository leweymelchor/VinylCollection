# Generated by Django 4.2.1 on 2023-05-30 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("records", "0010_alter_record_album"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="owner",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="record_owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
