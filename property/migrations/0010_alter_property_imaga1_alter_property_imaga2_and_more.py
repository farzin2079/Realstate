# Generated by Django 4.1.2 on 2023-04-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_alter_property_imaga1_alter_property_imaga2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='imaga1',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/property/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imaga2',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/property/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imaga3',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/property/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imaga4',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/property/%Y/%m/%d/'),
        ),
    ]
