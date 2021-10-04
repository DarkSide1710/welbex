# Generated by Django 2.2.2 on 2021-10-02 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud_ajax', '0002_auto_20211002_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='welbex',
            name='address',
        ),
        migrations.RemoveField(
            model_name='welbex',
            name='age',
        ),
        migrations.AddField(
            model_name='welbex',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='welbex',
            name='distance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='welbex',
            name='quantity',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]