from django.contrib import admin
from django.urls import path
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('otp/<mobile>', otp, name='otp'),
]
