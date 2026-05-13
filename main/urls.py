from django.urls import path
from . import views



urlpatterns=[
path ("",views.Home),
path('about/',views.about),
path('works/',views.works),
path('contan/',views.contan),
path('achiv/',views.achiev),

    
]