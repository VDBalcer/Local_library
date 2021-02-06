# Generated by Django 3.1.5 on 2021-02-06 14:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210206_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5cb11506-24ae-4f16-889c-8359d26117db'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
