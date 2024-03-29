# Generated by Django 4.2.10 on 2024-03-29 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200, unique=True)),
                ('productCode', models.CharField(max_length=200, unique=True)),
                ('dimensions', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('lastModified_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
