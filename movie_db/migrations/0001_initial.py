# Generated by Django 4.0.1 on 2022-01-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenreMovie',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('rating', models.CharField(max_length=3)),
                ('duration', models.CharField(max_length=10)),
                ('quality', models.CharField(max_length=10)),
                ('trailer', models.TextField()),
                ('watch', models.TextField()),
                ('genre', models.ManyToManyField(blank=True, to='movie_db.GenreMovie')),
            ],
        ),
    ]
