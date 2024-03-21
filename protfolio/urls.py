from django.urls import path
from .views import index
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "protfolio"
urlpatterns = [
    path("", index.as_view(), name="index"),
    path("send_mail/", views.send_mail_view, name="send_mail"),
    
   
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)