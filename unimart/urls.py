from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    # 2. Standard Admin (DO NOT use include() around admin.site.urls here)
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('products.urls', namespace='products')),  
    path('dashbord/', include('dashbord.urls')), 
    path('inbox/', include('messaging.urls')),
]


# The path can be a URL or a path to your static folder

handler404 = 'accounts.views.custom_404'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)