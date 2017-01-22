from django.conf.urls import include, url
from .views import YoMamaBotView
urlpatterns = [
                  url(r'^/?$', YoMamaBotView.as_view()) 
               ]