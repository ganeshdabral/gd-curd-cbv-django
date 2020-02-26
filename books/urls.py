from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
urlpatterns = [
	path('', BookListView.as_view(), name="list_view"),
	path('book/<slug>/',BookDetailView.as_view(), name="detail_view"),
	path('create/', BookCreateView.as_view(), name="create_view"),
	path('update/<slug>', BookUpdateView.as_view(), name="update_view"),
	path('delete/<slug>', BookDeleteView.as_view(), name="delete_view"),
]