from  django.urls import  path, include
from . import views
from  rest_framework.routers import DefaultRouter




app_name="post"

urlpatterns = [
    path("", views.index_view, name="home"),
]