# Generated by Django 3.0 on 2019-12-15 01:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vacationplanner', '0002_auto_20191215_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]