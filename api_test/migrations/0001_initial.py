# Generated by Django 3.0.7 on 2022-01-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('stu_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=20)),
                ('std', models.CharField(max_length=20)),
            ],
        ),
    ]
