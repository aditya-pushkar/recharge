# Generated by Django 4.0.3 on 2022-04-10 16:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('description', models.TextField()),
                ('validity', models.CharField(max_length=50)),
                ('ammount', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('active', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
