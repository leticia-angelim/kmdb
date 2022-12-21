# Generated by Django 4.1 on 2022-12-20 21:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("genres", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="genre",
            name="name",
            field=models.CharField(default=None, max_length=127),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="genre",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]