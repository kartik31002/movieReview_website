# Generated by Django 4.0.5 on 2022-07-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('director', models.CharField(max_length=350)),
                ('cast', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=5000)),
                ('release_date', models.DateField()),
                ('averageRating', models.FloatField()),
            ],
        ),
    ]
