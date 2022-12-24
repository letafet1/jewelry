# Generated by Django 2.2.28 on 2022-12-20 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='category_name')),
            ],
        ),
        migrations.CreateModel(
            name='Prods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='prods_name')),
                ('price', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='pos_img')),
                ('aciklama', models.TextField()),
                ('sale', models.IntegerField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_category', related_query_name='pcategory', to='post.Category')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name_plural': 'Prods',
                'verbose_name': 'Prod',
            },
        ),
    ]