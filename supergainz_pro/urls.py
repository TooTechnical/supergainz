from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # handles /signup, /login, /logout
    path('', include('users.urls')),
    path('payments/', include('payments.urls')),
    path('products/', include('products.urls')),
    path('newsletter/', include('newsletters.urls')),


]

