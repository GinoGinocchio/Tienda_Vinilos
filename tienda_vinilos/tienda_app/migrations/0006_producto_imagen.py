# Generated by Django 3.1.4 on 2020-12-31 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0005_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
