# Generated by Django 2.1.3 on 2019-02-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scand', '0017_auto_20190218_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagetag',
            name='is_reverted',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]