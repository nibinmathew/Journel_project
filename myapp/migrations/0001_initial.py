# Generated by Django 2.2.6 on 2019-10-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' Enter your unique Id here', max_length=20)),
                ('password', models.CharField(help_text=' Enter your password ', max_length=15)),
            ],
        ),
    ]
