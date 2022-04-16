# Generated by Django 4.0.3 on 2022-04-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config_key', models.CharField(max_length=50)),
                ('config_value', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='got_lottery',
            field=models.BooleanField(default=False, help_text='是否中奖'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='has_purchased',
            field=models.BooleanField(default=False, help_text='是否已经购买'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.IntegerField(default=0, help_text='奖金金额'),
        ),
    ]