# Generated by Django 3.1.4 on 2021-01-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0012_orden_ordenproducto_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='codigo_postal',
            field=models.CharField(max_length=200, null=True),
        ),
    ]