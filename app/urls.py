from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('class-list', views.workoutclass_list, name='workoutclass')
]
