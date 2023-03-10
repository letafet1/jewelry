# Generated by Django 2.2.28 on 2022-12-24 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='prods',
            name='aciklama',
        ),
        migrations.AddField(
            model_name='prods',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='prods',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='category_name'),
        ),
        migrations.AlterField(
            model_name='prods',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='prods_name'),
        ),
        migrations.AlterField(
            model_name='prods',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='prods',
            name='sale',
            field=models.IntegerField(null=True),
        ),
    ]
