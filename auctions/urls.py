from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_auction", views.create_auction, name="create_auction"),
    path("auction/<int:auction_id>", views.page_auction, name="page_auction"),
    path("auction/<int:auction_id>/comment", views.post_comment, name="post_comment"),
    path("auction/<int:auction_id>/bid", views.make_bid, name="make_bid"),
    path("auction/<int:auction_id>/closeauction", views.close_auction, name="close_auction"),
    path("auction/<int:auction_id>/watchlist", views.toggle_watchlist, name="toggle_watchlist"),
    path("watchlist", views.get_watchlist, name="get_watchlist"),
    path("categories", views.categories, name="categories"),
    path("category_page<str:category>",views.category_page, name="category_page" )
]
