# Generated by Django 4.1.1 on 2024-05-28 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0014_movie_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('date_of_birth', models.DateField(null=True)),
                ('date_of_death', models.DateField(null=True)),
                ('place_of_birth', models.CharField(max_length=32, null=True)),
                ('place_of_death', models.CharField(max_length=32, null=True)),
                ('biography', models.TextField(null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viewer.country')),
            ],
            options={
                'verbose_name_plural': 'People',
                'ordering': ['surname', 'name', 'date_of_birth'],
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='acts', to='viewer.people'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(blank=True, related_name='directs', to='viewer.people'),
        ),
    ]
