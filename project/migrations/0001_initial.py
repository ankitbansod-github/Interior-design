# Generated by Django 3.1.3 on 2020-11-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Office', 'Office'), ('Residential', 'Residential'), ('Commercial', 'Commercial')], max_length=50, null=True)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
