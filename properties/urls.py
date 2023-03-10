from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='home'),
    path('property_list/', views.property_list, name='property_list'),
    path('<int:pk>/', views.property_detail, name='property_detail'),
    path('new/', views.create_property, name='property_create'),
    path('<int:property_id>/edit/', views.edit_property, name='property_update'),
    path('<int:property_id>/upload_photo/', views.upload_property_photo, name='upload_property_photo'),
    path('<int:pk>/delete/', views.property_delete, name='property_delete'),
]
