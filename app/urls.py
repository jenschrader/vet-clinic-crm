from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('view/<int:pk>', views.view_client, name='view'),
    path('delete/<int:pk>', views.delete_client, name='delete'),
    path('create/', views.create_client, name='create'),
    path('edit/<int:pk>', views.edit_client, name='edit'),
    path('add_pet/<int:client_id>', views.add_pet, name='add-pet'),
    path('edit_pet/<int:pk>', views.edit_pet, name='edit-pet'),
    path('delete_pet/<int:pk>', views.delete_pet, name='delete-pet'),

]