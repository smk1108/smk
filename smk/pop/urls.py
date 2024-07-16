from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index_show),
    path('detail/<int:pk>/', views.detail_show,name = 'detail')
]