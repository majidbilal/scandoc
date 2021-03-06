# Generated by Django 2.1.3 on 2019-02-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scand', '0014_auto_20190210_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetag',
            name='accoff',
            field=models.CharField(max_length=200, verbose_name='Office / Deptt:'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='company',
            field=models.CharField(max_length=200, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='docref',
            field=models.CharField(max_length=10, verbose_name='Document Ref.'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='section',
            field=models.CharField(max_length=200, verbose_name='Section'),
        ),
    ]
