# Generated by Django 5.0.4 on 2024-05-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateField()),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('architector', models.CharField(max_length=40)),
                ('foundation_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Здание',
                'verbose_name_plural': 'Здания',
            },
        ),
    ]
