# Generated by Django 4.2.1 on 2023-05-14 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='user name')),
                ('password', models.CharField(max_length=64, verbose_name='password')),
                ('age', models.IntegerField(default=0, verbose_name='age')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='account balance')),
                ('create_time', models.DateTimeField(verbose_name='create time')),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'femal')], verbose_name='gender')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
    ]