# Generated by Django 3.2.6 on 2021-08-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_auto_20210827_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('postal_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AddField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(to='book_outlet.Country'),
        ),
    ]
