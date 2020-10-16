from django.urls import path
from . import views

urlpatterns=[
  path('',views.wasserstand_list, name='wasserstand_list')
]
