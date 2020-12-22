from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('user_detail/<int:user_id>', views.user_detail, name='user_detail'),
    path('add_to_shopping_cart/<int:book_id>', views.add_to_shopping_cart, name='add_to_shopping_cart'),
    path('remove_shopping_cart/<int:book_id>', views.remove_shopping_cart, name='remove_shopping_cart'),
    path('remove_in_shopping_cart/<int:book_id>', views.remove_in_shopping_cart, name='remove_in_shopping_cart'),
    path('postbook', views.postbook, name='postbook'),
    path('requestbook', views.requestbook, name='requestbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('displayusers', views.displayusers, name='displayusers'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('about_page', views.about_page, name='about_page'),
    path('about_us', views.about_us, name='about_us'),
    path('searchbar', views.searchbar, name='searchbar'),
    path('sorting', views.sorting, name='sorting'),
    path('buybooks', views.buybooks, name='buybooks'),
]