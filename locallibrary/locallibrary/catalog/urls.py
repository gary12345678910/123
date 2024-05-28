from django.conf.urls import include
from django.urls import path
from catalog import views

# app_name = "catalog"
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>',views.BookDetailView.as_view(), name = 'book-detail'),
    path('authors', views.AuthorListView.as_view(), name = 'authors'),
    path('author/<int:pk>',views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

