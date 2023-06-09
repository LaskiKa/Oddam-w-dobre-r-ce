# Generated by Django 4.2 on 2023-04-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putingoodhands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('type', models.SmallIntegerField(choices=[(1, 'Fundacja'), (2, 'Organizacja pozarządowa'), (3, 'Zbiórka lokalna')], default=1)),
                ('categories', models.ManyToManyField(to='putingoodhands.category')),
            ],
        ),
    ]
