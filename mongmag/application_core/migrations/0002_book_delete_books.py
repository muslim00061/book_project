# Generated by Django 4.1.13 on 2024-03-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Кітаптың аты')),
                ('discription', models.CharField(max_length=400, verbose_name='Описание')),
                ('image', models.CharField(max_length=1000, verbose_name='Ссылка на изображения')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
        migrations.DeleteModel(
            name='books',
        ),
    ]