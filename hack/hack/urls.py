from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('account.urls')),
    path('board/',include('board.urls')),
    path('',include('main_page.urls')),
]
