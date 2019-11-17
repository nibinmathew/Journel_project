# Generated by Django 2.2.6 on 2019-11-17 21:11

from django.db import migrations, models
import login.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siteuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, validators=[login.validators.validate_firstname_length], verbose_name='First name')),
                ('lastname', models.CharField(max_length=100, validators=[login.validators.validate_lastname_length], verbose_name='Last name')),
                ('username', models.CharField(max_length=25, validators=[login.validators.validate_username_length, login.validators.validate_username_alphadigits], verbose_name='User name')),
                ('password1', models.CharField(max_length=30, validators=[login.validators.validate_password_length, login.validators.validate_password_digit, login.validators.validate_password_uppercase])),
                ('password2', models.CharField(max_length=30)),
                ('birth_date', models.DateField(verbose_name='What is your birth date?')),
                ('gender', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, validators=[login.validators.validate_phonenumber])),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]