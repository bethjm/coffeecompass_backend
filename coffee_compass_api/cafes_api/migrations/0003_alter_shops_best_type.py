# Generated by Django 4.2 on 2023-04-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes_api', '0002_remove_shops_flavor_notes_remove_shops_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='best_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
