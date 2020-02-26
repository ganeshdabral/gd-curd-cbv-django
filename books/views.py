from django.urls import reverse
from django.shortcuts import render
from .models import BookModel
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import BookForm

class BookListView(ListView):
	model = BookModel
	template_name = "book/list.html"

class BookDetailView(DetailView):
	model = BookModel
	template_name = "book/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(BookDetailView, self).get_context_data(*args, **kwargs)
		context["title"] = "Detail View"
		return context

class BookCreateView(CreateView):
	model = BookModel
	template_name = "book/create.html"
	form_class = BookForm

	def form_valid(self, form):
		return super(BookCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("detail_view",kwargs={"slug": self.object.slug})

class BookUpdateView(UpdateView):
	model = BookModel
	template_name = "book/create.html"
	form_class = BookForm

	def get_success_url(self):
		return reverse("detail_view", kwargs={"slug": self.object.slug})

class BookDeleteView(DeleteView):
	model = BookModel
	template_name = "book/delete.html"
	def get_success_url(self):
		return reverse("list_view")
