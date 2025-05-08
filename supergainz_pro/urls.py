from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('users.urls')),
    path('dashboard/', include('users.urls')),
    path('payments/', include('payments.urls')),
    path('products/', include('products.urls')),
    path('newsletter/', include('newsletters.urls')),
]

# ✅ Append media serving for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
