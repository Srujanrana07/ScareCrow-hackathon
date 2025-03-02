#disease_detector\urls.py
from django.urls import path
from .views import home, predict_crop_view, index2,detect_disease, ask_question

urlpatterns = [
    path('', home, name="home"),
    path('predict_crop/', predict_crop_view, name="predict_crop"),
    path('index2/', index2, name='index2'),
    path('detect_disease/', detect_disease, name='detect_disease'),
    path("ask_question/", ask_question, name="ask_question"),

]
