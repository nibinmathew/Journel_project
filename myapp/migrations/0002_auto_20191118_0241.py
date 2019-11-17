# Generated by Django 2.2.6 on 2019-11-17 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('email_id', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]