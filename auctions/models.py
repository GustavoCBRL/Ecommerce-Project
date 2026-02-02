from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist = models.ManyToManyField('Auction', blank=True, related_name="watchers")
    pass

class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(default="")
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image_url = models.URLField(blank=True)
    category = models.CharField(max_length=64, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")

    def __str__(self):
        return f"{self.title}"
    
    def status(self):
        return "Open" if self.is_active else "Closed"


class Bid(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids")
    timestamp = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-value']

    def __str__(self):
        return f"$ {self.value} on {self.auction.title}"
    

    
class Comment(models.Model):
    text = models.CharField (max_length = 3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.author.username} on {self.auction.title}"
    

