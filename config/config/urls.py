from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "TECO Administration"
admin.site.site_title = "TECO Admin Portal"
admin.site.index_title = "Welcome to TECO Management"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('news.urls')), # Connect our news API
]

# Allow Django to serve images during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)