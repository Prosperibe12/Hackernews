from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('show/', views.show_category, name='show'),
    path('jobs/', views.job_category, name='jobs'),
    path('ask/', views.ask_category, name='ask'),
    path('ask-details/<str:id>/', views.ask_details, name='ask-details')
]