# Generated by Django 3.2.7 on 2022-02-07 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0005_rename_component_item_comp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='comp',
        ),
        migrations.AddField(
            model_name='item',
            name='menu_items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='cuisine.menu'),
        ),
    ]
