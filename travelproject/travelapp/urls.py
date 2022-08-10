from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),

    # path('aboutme/',views.aboutme,name='aboutme'),
    # path('contact/',views.contact,name="contact")
    # path('add/',views.addition,name='addition')
]