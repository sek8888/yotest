from django.conf.urls import include, url
from .views import YoMamaBotView
urlpatterns = [
                  url(r'^m/?$', YoMamaBotView.as_view()) 
               ]
