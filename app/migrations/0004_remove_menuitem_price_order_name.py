# Generated by Django 5.1.2 on 2024-12-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_order_item_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='Unknown', max_length=15),
            preserve_default=False,
        ),
    ]
