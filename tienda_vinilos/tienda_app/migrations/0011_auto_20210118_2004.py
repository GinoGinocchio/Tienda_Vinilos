# Generated by Django 3.1.4 on 2021-01-19 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0010_auto_20210118_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='artista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tienda_app.artista'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='genero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tienda_app.genero'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]