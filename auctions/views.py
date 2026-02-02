from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import User, Auction, Bid, Comment


def index(request):
    auctions = Auction.objects.all()

    return render(request, "auctions/index.html", {
       "auctions": auctions
   })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_auction(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        image_url = request.POST.get("image_url", "")
        category = request.POST.get("category", "")
        
        # Create new auction
        auction = Auction.objects.create(
            title=name,
            description=description,
            starting_bid=starting_bid,
            image_url=image_url,
            category=category,
            seller=request.user,
            is_active=True
        )
        
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create_auction.html")

def page_auction(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    comments = auction.comments.all()
    bids = auction.bids.all()
    current_bid = bids.first() if bids.exists() else None
    
    return render(request, "auctions/page_auction.html", {
        "auction": auction,
        "comments": comments,
        "current_bid": current_bid
    })

def post_comment(request, auction_id):
    if request.method == "POST":
        text = request.POST.get("text", "")
        auction = get_object_or_404(Auction, pk=auction_id)

        if text: 
            Comment.objects.create(
                text=text,
                author=request.user,
                auction=auction
            )

        return redirect("page_auction", auction_id=auction_id)
    
    return redirect("index")

def get_comment(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    comments = auction.comments.all()

    return render(request, "auctions/page_auction.html", {
        "auction": auction,
        "comments": comments
    })

def make_bid(request, auction_id):
    if request.method == "POST":
        value = request.POST.get("value", "")
        auction = get_object_or_404(Auction, pk=auction_id)

        if value:
            Bid.objects.create(
                bidder=request.user,
                value=value,
                auction=auction
            )
        return redirect("page_auction", auction_id=auction_id)
    
    return redirect("index")
  
def get_currentbid(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    
    # Pega todos os lances (bids) relacionados a este leilão
    bids = auction.bids.all()
    bids_number = bids.count()
    
    # Pega o lance mais recente/maior
    current_bid = bids.first() if bids.exists() else None
    
    return render(request, "auctions/page_auction.html", {
        "auction": auction,
        "bids": bids, 
        "bids_number": bids_number, 
        "current_bid": current_bid
    })



def toggle_watchlist(request, auction_id):
    if not request.user.is_authenticated:
        return redirect("login")
    
    auction = get_object_or_404(Auction, pk=auction_id)
    
    if auction in request.user.watchlist.all():
        request.user.watchlist.remove(auction)
    else:
        request.user.watchlist.add(auction)
    
    return redirect("page_auction", auction_id=auction_id)

def get_watchlist(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    watchlist = request.user.watchlist.all()

    return render(request, "auctions/whatchlist.html", {
        "watchlist": watchlist
    })

def close_auction(request, auction_id):
    if request.method == "POST":
        auction = get_object_or_404(Auction, pk=auction_id)
       
        if request.user == auction.seller:
            auction.is_active = False
            auction.save()
        
        return redirect("page_auction", auction_id=auction_id)
    
    return redirect("index")

def categories(request):
    selected_category = request.GET.get("category", None)
    if selected_category:
        auctions = Auction.objects.filter(category=selected_category)
    else:
        auctions = Auction.objects.all()
        category = Auction.objects.values_list('category', flat=True).distinct()
    
    return render(request, "auctions/categories.html", {
        "auctions": auctions,
        "category": category,
        "selected_category": selected_category
    })

def category_page(request, category):
    auctions = Auction.objects.filter(category=category)
    return render(request, "auctions/category_page.html", {
        "auctions": auctions,
        "category": category
    })