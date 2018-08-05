from django.urls import path

from . import views

app_name = 'opinion'

urlpatterns = [
    path('', views.list_all, name='list_all'),
    path('', views.list_all, name='index'),
    path('<int:opinion_id>/', views.show_opinion, name='show_opinion'),
    path('item/<int:item_id>/add_opinion/', views.add_opinion, name='add_opinion'),
    path('<int:opinion_id>/edit/', views.edit_opinion, name='edit_opinion'),
    path('<str:table>/add/', views.add_category_or_item, name='add_category_or_item'),
    path('delete/', views.delete_opinion, name='delete_opinion'),
]
