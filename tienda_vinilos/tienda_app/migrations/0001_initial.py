# Generated by Django 2.2.3 on 2020-12-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=30)),
            ],
        ),
       
    ]
