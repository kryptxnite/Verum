# Generated by Django 4.2.11 on 2024-04-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='preview/'),
        ),
        migrations.AddField(
            model_name='post',
            name='thematic_picture',
            field=models.ImageField(blank=True, null=True, upload_to='thematic/'),
        ),
    ]
