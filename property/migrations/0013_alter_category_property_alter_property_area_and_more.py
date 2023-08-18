# Generated by Django 4.1.2 on 2023-08-18 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_profile_image'),
        ('property', '0012_rename_imaga1_property_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='property',
            field=models.ManyToManyField(related_name='property_category', to='property.property'),
        ),
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='property.category'),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='value',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='vpm',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='watchlist',
            field=models.ManyToManyField(related_name='Profile_watch', to='account.profile'),
        ),
    ]
