# Generated by Django 3.1.5 on 2021-02-06 14:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20210206_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6ff2184d-47e3-4a8a-8da8-ebcd1ced9dc6'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]