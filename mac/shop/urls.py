from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="ShopHome"),                            # this is the first page u will see
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('tracker/',views.track,name="trackingstatus"),
    path('prodview/',views.prodview,name="product_view"),
    path('checkout/',views.checkout,name="checkout"),

]