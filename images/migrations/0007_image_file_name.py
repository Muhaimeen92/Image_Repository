# Generated by Django 3.2.7 on 2021-09-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='file_name',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
