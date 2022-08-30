from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='Home'),
    path('index_sent/', views.Index1.as_view(), name='send-notification'),
    path('index_sent1/', views.Index2.as_view(), name='send-notification'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
