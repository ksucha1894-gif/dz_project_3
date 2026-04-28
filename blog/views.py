from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Blog

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blog"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"


class BlogCreateView(CreateView):
    model = Blog
    fields = ("name", "description", "image", "publication_sign", "view_count")
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("name", "description", "image", "publication_sign", "view_count")
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
