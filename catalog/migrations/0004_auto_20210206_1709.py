# Generated by Django 3.1.5 on 2021-02-06 14:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210206_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('325877dd-c337-4ebc-8f0e-21ecf6061516'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]