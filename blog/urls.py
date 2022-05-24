from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('curso', views.curso, name='curso'),
    path('modelform', views.form_modelform, name ='formulario'),
    ]
