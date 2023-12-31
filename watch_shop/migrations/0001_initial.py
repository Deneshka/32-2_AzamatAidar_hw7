# Generated by Django 4.2.5 on 2023-10-05 11:00

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_object', models.CharField(max_length=100, verbose_name='Укажите название часов:')),
                ('review_created_at', models.DateTimeField(auto_now_add=True)),
                ('review_text', models.TextField(blank=True, null=True, verbose_name='Отзыв:')),
                ('review_start', models.CharField(choices=[('Оценка: 1', 'Оценка: 1'), ('Оценка: 2', 'Оценка: 2'), ('Оценка: 3', 'Оценка: 3'), ('Оценка: 4', 'Оценка: 4'), ('Оценка: 5', 'Оценка: 5')], max_length=100, verbose_name='Укажите свою оценку:')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.IntegerField(choices=[(1, 'Администратор'), (2, 'VIP Клиент'), (3, 'Клиент')], verbose_name='Выберите тип пользователя')),
                ('phone_number', models.CharField(max_length=13, verbose_name='ваш сотовый:')),
                ('age', models.PositiveIntegerField(default=15, verbose_name='Укажите возраст?')),
                ('gender', models.IntegerField(choices=[(1, 'М'), (2, 'Ж')], verbose_name='Ваш пол')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Укажите название часов:')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание часов:')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Добавьте фото часов:')),
                ('review', models.URLField(verbose_name='Укажите ссылку')),
                ('model', models.CharField(choices=[('B650WB-1B', 'B650WB-1B'), ('MTP-VD03B-1A', 'MTP-VD03B-1A'), ('MTP-1308D-1A', 'MTP-1308D-1A'), ('MTP-VD01G-1B', 'MTP-VD01G-1B')], max_length=100, verbose_name='Укажите модель часов:')),
                ('cost', models.PositiveIntegerField(verbose_name='Укажите цену часов:')),
                ('director', models.CharField(max_length=100, null=True, verbose_name='Укажите авторство:')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Часы',
                'verbose_name_plural': 'Часы',
            },
        ),
    ]
