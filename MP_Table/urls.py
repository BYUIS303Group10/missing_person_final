from django.urls import path
from .views import indexPageView
from .views import postPageView
from .views import aboutPageView, personView
            
urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("post/", postPageView, name="post"),
    path('person/', personView, name='person')
]  
