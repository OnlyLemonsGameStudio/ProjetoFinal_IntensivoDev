# Generated by Django 4.1.2 on 2022-10-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeboy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itens', models.ManyToManyField(to='homeboy.produto')),
            ],
        ),
    ]