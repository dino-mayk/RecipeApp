# Generated by Django 3.2 on 2023-04-16 18:27

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('description', tinymce.models.HTMLField(help_text='введите ваше описание рецепта', verbose_name='описание')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='дата создания', verbose_name='дата создания')),
                ('photo', models.ImageField(help_text='загрузите картинку', null=True, upload_to='uploads/preview/%Y/%m', verbose_name='картинка')),
                ('food_type', models.PositiveSmallIntegerField(choices=[(1, 'салат'), (2, 'мясо'), (3, 'рыба')], default=3, verbose_name='тип рецепта')),
            ],
            options={
                'verbose_name': 'рецепт',
                'verbose_name_plural': 'рецепты',
            },
        ),
        migrations.CreateModel(
            name='RecipeGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(help_text='загрузите картинку', upload_to='uploads/gallery/%Y/%m', verbose_name='картинка')),
                ('recipe', models.ForeignKey(help_text='выберете рецепт', on_delete=django.db.models.deletion.CASCADE, to='apis.recipe', verbose_name='рецепт')),
            ],
            options={
                'verbose_name': 'фотографию рецепта',
                'verbose_name_plural': 'фотогалерея рецептов',
            },
        ),
    ]
