# Generated by Django 4.2.8 on 2023-12-17 21:33

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_content', '0011_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
