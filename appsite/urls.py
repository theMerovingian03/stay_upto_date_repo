from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('whyto/', views.whyto, name='whyto'),
    path('team/<str:member_id>/', views.team, name='team'),
    path('email_status/', views.email_status, name='email_status'),
    path('pricing/',views.pricing,name='pricing'),
    path('industry/<str:choice>/',views.industry,name='industry'),
    path('all_industries/',views.all_industries,name='all_industries'),
    path('email_error/',views.email_error, name='email_error')
]
