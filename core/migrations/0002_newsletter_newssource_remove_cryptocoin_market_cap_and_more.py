# Generated by Django 5.1.7 on 2025-03-25 22:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('recipients_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('scraping_config', models.JSONField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cryptocoin',
            name='market_cap',
        ),
        migrations.RemoveField(
            model_name='cryptocoin',
            name='percent_change_24h',
        ),
        migrations.RemoveField(
            model_name='cryptocoin',
            name='percent_change_30d',
        ),
        migrations.RemoveField(
            model_name='cryptocoin',
            name='percent_change_60d',
        ),
        migrations.RemoveField(
            model_name='cryptocoin',
            name='percent_change_7d',
        ),
        migrations.RemoveField(
            model_name='cryptocoin',
            name='percent_change_90d',
        ),
        migrations.RemoveField(
            model_name='cryptocoin',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cryptocoin',
            name='volume_24h',
        ),
        migrations.AddField(
            model_name='cryptocoin',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='CryptoNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(unique=True)),
                ('raw_content', models.TextField()),
                ('summary', models.TextField()),
                ('sentiment', models.FloatField(blank=True, null=True)),
                ('published_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coins', models.ManyToManyField(to='core.cryptocoin')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.newssource')),
            ],
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=8, max_digits=20)),
                ('market_cap', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('timestamp', models.DateTimeField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cryptocoin')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subscribed_coins', models.ManyToManyField(to='core.cryptocoin')),
            ],
        ),
    ]
