
from django.urls import path
from home import views

app_name='Home'

urlpatterns = [
    path('',views.home,name='home'),
    path('order/',views.place_order_page,name='place_order_page'),
    path('profile/',views.profile,name='profile'),
    path('reciveorder/',views.reciveOrder,name='reciveorder'),
    path('paytm_confirmation/',views.paytm_confirmation,name='paytmConfirmation'),
]
