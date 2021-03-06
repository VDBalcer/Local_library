# Generated by Django 3.1.5 on 2021-02-06 14:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210206_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('07cf52bf-bd3f-4226-bd35-3506aed0fb27'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
