

from django.contrib import admin
from django.urls import path

from rgb.views import UserList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserList.as_view(), name='user-list'),
]
