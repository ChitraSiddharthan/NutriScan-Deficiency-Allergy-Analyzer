from django.contrib import admin
from django.urls import path, include
from user_management import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user_management.urls')),
    path('api/', include('user_management.urls')), # API routes
    path('accounts/', include('django.contrib.auth.urls')), #helps django to display the user login
    path('', user_views.home, name='home'), #homepage
]
