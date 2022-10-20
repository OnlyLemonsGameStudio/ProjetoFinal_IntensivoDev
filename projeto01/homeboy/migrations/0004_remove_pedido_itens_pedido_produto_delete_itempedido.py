# Generated by Django 4.1.1 on 2022-10-20 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeboy', '0003_itempedido_alter_pedido_itens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='itens',
        ),
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homeboy.produto'),
        ),
        migrations.DeleteModel(
            name='ItemPedido',
        ),
    ]
