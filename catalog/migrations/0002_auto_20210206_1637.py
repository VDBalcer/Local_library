# Generated by Django 3.1.5 on 2021-02-06 13:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0cb67b63-0aab-40e4-85cb-3fb0436d4de1'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
