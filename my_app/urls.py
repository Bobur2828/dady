
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('main/', views.main, name='main'),
    path('single/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
    path('departament/', views.departament, name='departament'),
    path('doctors/', views.doctors, name='doctors'),
    path('elements/', views.elements, name='elements'),
    path('showdoc/<int:pk>/', views.showdoctor, name='showdoc'),
    

]
