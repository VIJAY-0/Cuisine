
from django.urls import path
from Accounts import views

app_name='Accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_,name='login'),
    path('logout',views.logout_,name='logout'),
]
