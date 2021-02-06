# Generated by Django 3.1.5 on 2021-02-06 14:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20210206_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b2d03f9d-3ef2-4976-99b7-dd0a07f971f9'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
