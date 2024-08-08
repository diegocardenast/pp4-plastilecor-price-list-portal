# Generated by Django 4.2.10 on 2024-08-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceList', '0004_alter_listitem_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='dimensions',
        ),
        migrations.AddField(
            model_name='listitem',
            name='heightDimension',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listitem',
            name='lengthDimension',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listitem',
            name='widthDimension',
            field=models.IntegerField(null=True),
        ),
    ]
