# Generated by Django 2.1.3 on 2019-02-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scand', '0015_auto_20190212_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetag',
            name='accoff',
            field=models.CharField(help_text='required field', max_length=200, verbose_name='Office / Deptt: ❗'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='attr1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Extra Attribute'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='attr2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Extra Attribute'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='attr3',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Extra Attribute'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='attr4',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Extra Attribute'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='attr5',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Extra Attribute'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='company',
            field=models.CharField(help_text='required field', max_length=200, verbose_name='Company ❗'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='docref',
            field=models.CharField(help_text='required field', max_length=10, verbose_name='Document Ref. ❗'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='pagenum',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Page Number'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='pernum',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Personnel Id No.'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='refnum',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Reference Number'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='section',
            field=models.CharField(help_text='required field', max_length=200, verbose_name='Section ❗'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='status',
            field=models.CharField(blank=True, choices=[('01', 'created'), ('02', 'proofread'), ('03', 'active')], max_length=2, null=True),
        ),
    ]