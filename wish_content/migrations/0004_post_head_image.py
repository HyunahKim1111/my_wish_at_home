# Generated by Django 4.2.8 on 2023-12-14 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_content', '0003_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='wish_content/images/%Y/%m/%d/'),
        ),
    ]
