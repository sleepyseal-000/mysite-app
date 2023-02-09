from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage),

    path('insert_to_do/', views.insert_to_do_item, name='insert_to_do_item'),
    path('insert_to_cook/', views.insert_to_cook_item, name='insert_to_cook_item'),
    path('insert_to_wish/', views.insert_to_wish_item, name='insert_to_wish_item'),


    path('delete_to_do/<int:to_do_id>/', views.delete_to_do_item, name='delete_to_do_item'),
    path('delete_to_cook/<int:to_cook_id>/', views.delete_to_cook_item, name='delete_to_cook_item'),
    path('delete_to_wish/<int:to_wish_id>/', views.delete_to_wish_item, name='delete_to_wish_item'),

]

