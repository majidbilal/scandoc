# Generated by Django 2.1.3 on 2019-02-06 20:16

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scand', '0012_auto_20190207_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetag',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2019, 2, 6, 20, 15, 57, 27912, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
