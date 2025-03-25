from django.db import models
from django.utils import timezone

class CryptoCoin(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class NewsSource(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    scraping_config = models.JSONField()  # Para configurar selectores CSS/XPATH

class CryptoNews(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    raw_content = models.TextField()
    summary = models.TextField()
    sentiment = models.FloatField(null=True, blank=True)  # -1 a 1
    coins = models.ManyToManyField(CryptoCoin)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class PriceHistory(models.Model):
    coin = models.ForeignKey(CryptoCoin, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    volume = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    timestamp = models.DateTimeField()

class Newsletter(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    recipients_count = models.IntegerField()

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    subscribed_coins = models.ManyToManyField(CryptoCoin)
    created_at = models.DateTimeField(auto_now_add=True)