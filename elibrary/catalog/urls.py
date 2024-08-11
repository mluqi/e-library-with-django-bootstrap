from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.book_list, name="list"),
    path('add/', views.add_book, name='add_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]