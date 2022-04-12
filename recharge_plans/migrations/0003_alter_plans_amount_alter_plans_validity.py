# Generated by Django 4.0.3 on 2022-04-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recharge_plans', '0002_rename_ammount_plans_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='amount',
            field=models.PositiveIntegerField(default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='plans',
            name='validity',
            field=models.PositiveIntegerField(max_length=2),
        ),
    ]
