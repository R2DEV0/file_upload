from django.urls import path     
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index ),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('detail/<int:carrier_id>', views.detail),
    path('logout', views.logout),
    path('addNew', views.addNew)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)