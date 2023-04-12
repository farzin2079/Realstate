# Generated by Django 4.1.2 on 2023-04-10 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_alter_property_imaga1_alter_property_imaga2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='property_category', to='property.property'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imaga1',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/<django.db.models.query_utils.DeferredAttribute object at 0x000002502480DC00>'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imaga2',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/<django.db.models.query_utils.DeferredAttribute object at 0x000002502480DC00>'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imaga3',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/<django.db.models.query_utils.DeferredAttribute object at 0x000002502480DC00>'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imaga4',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/<django.db.models.query_utils.DeferredAttribute object at 0x000002502480DC00>'),
        ),
    ]