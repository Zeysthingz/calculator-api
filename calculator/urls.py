
from django.urls import path

#vewsin tamamını import et demektir.
from . import views    

urlpatterns = [
    path('',views.index, name='index'),
]
