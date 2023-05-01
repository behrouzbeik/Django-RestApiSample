# Generated by Django 4.2 on 2023-04-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('stdnum', models.IntegerField()),
                ('teacher', models.CharField(choices=[('ahmadi', 'Ahmadi'), ('abdi', 'Abdi'), ('bahrami', 'Bahrami')], max_length=7)),
            ],
            options={
                'ordering': ['stdnum'],
            },
        ),
    ]
