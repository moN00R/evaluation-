# Generated by Django 5.1.1 on 2024-09-24 19:35

import common.fields.location
import common.fields.price
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_mymodel_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='time',
        ),
        migrations.AddField(
            model_name='mymodel',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='deleted_by_cascade',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='end_date',
            field=models.DateTimeField(default='2020-09-25 06:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='last_price',
            field=common.fields.price.PriceField(decimal_places=8, default=111, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='latitude',
            field=common.fields.location.LatitudeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='longitude',
            field=common.fields.location.LongitudeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='price',
            field=common.fields.price.PriceField(decimal_places=8, default=121, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='start_date',
            field=models.DateTimeField(default='2019-09-25 06:00 '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
