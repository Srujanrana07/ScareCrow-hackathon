from django.urls import path
from .views import home, predict_crop_view

urlpatterns = [
    path('', home, name="home"),
    path('predict_crop/', predict_crop_view, name="predict_crop"),
]
