from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('ecommerce.template_urls')),
    path('api/', include('ecommerce.urls')),
    path('admin/', admin.site.urls),
]

# Serve media and static files during development or as fallback
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
