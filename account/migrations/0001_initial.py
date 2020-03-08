# Generated by Django 3.0.2 on 2020-03-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default=' ', max_length=50)),
                ('lastname', models.CharField(default=' ', max_length=50)),
                ('email', models.EmailField(default='xyz', max_length=60, unique=True, verbose_name='email')),
                ('gender', models.CharField(default=' ', max_length=50)),
            ],
        ),
    ]