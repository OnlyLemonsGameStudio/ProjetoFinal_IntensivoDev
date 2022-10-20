# Generated by Django 4.1.2 on 2022-10-20 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeboy', '0002_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homeboy.produto')),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='itens',
            field=models.ManyToManyField(to='homeboy.itempedido'),
        ),
    ]
