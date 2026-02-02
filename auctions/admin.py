from django.contrib import admin

from .models import User, Bid, Auction, Comment

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

class BudAdmin(admin.ModelAdmin):
    list_display = ('value', 'bidder', 'auction')

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'auction')

admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Auction)
admin.site.register(Comment)

# Register your models here.
