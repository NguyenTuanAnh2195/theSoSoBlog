from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import BlogUser, Post
from .forms import UserRegisterForm
# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')

    if request.method == 'GET':
        form = UserRegisterForm()

    return render(
            request,
            'blogapp/register.html',
            {'form': form}
        )


class BlogUserDetailView(DetailView):
    model = BlogUser


class BlogUserListView(ListView):
    model = BlogUser
    paginate_by = 10


class PostListView(ListView):
    model = Post
    paginate_by = 10
