# Generated by Django 5.0.7 on 2024-08-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuessNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('text', models.CharField(max_length=200)),
                ('lottos', models.CharField(default='[1,2,3,4,5,6]', max_length=255)),
                ('num_lotto', models.IntegerField(default=5)),
                ('updated_date', models.DateTimeField()),
            ],
        ),
    ]
