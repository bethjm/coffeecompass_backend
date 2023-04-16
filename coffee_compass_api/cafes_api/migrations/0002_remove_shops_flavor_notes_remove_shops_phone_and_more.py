# Generated by Django 4.2 on 2023-04-16 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shops',
            name='flavor_notes',
        ),
        migrations.RemoveField(
            model_name='shops',
            name='phone',
        ),
        migrations.AddField(
            model_name='shops',
            name='acidic',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='berry',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='best_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='bitter',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='caramel',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='chocolate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='citrus',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='floral',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='smoky',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='sweet',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
