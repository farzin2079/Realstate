# Generated by Django 4.1.2 on 2023-04-10 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_created_alter_profile_image_and_more'),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='imaga2',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/<django.db.models.query_utils.DeferredAttribute object at 0x000001AF3E87DBD0>'),
        ),
        migrations.AddField(
            model_name='property',
            name='imaga3',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/<django.db.models.query_utils.DeferredAttribute object at 0x000001AF3E87DBD0>'),
        ),
        migrations.AddField(
            model_name='property',
            name='imaga4',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/<django.db.models.query_utils.DeferredAttribute object at 0x000001AF3E87DBD0>'),
        ),
        migrations.AlterField(
            model_name='property',
            name='imaga1',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='photo/<django.db.models.query_utils.DeferredAttribute object at 0x000001AF3E87DBD0>'),
        ),
        migrations.AlterField(
            model_name='property',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='Profile_watch', to='account.profile'),
        ),
    ]