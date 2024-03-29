
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('backend.urls')),
    path('',include('store.urls')),
    path('',include('cartt.urls')),
    path('',include('register.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
