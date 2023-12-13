# Generated by Django 4.2 on 2023-12-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('curso', models.CharField(max_length=20)),
                ('promedio', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]