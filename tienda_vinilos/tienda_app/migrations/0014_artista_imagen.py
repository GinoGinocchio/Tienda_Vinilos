# Generated by Django 3.1.4 on 2021-01-31 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0013_auto_20210122_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='artistas'),
        ),
    ]
