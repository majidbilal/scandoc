# Generated by Django 2.1.3 on 2019-02-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scand', '0021_auto_20190218_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetag',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'created'), (2, 'proofread'), (3, 'active')], max_length=2, null=True),
        ),
    ]