# Generated by Django 3.1.4 on 2020-12-31 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0004_auto_20201215_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]