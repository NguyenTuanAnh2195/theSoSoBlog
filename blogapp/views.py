from typing import Any

from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import (
    ListView, CreateView, DetailView, DeleteView, UpdateView
)
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
)

from django.contrib.auth.decorators import login_required

from .models import Post, Like
from .forms import PostCreateForm
# Create your views here.


class PostListView(ListView):
    template_name = 'blogapp/index.html'
    model = Post
    paginate_by = 10
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'blogapp/post_detail.html'
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blogapp/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('blogs:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        profile = self.request.user.profile
        kwargs.update({'author': profile})
        return kwargs


class PostOwnerPermissionMixin(PermissionRequiredMixin):
    def dispatch(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any
    ) -> HttpResponse:

        if not request.user.is_authenticated:
            return redirect('accounts:login')

        # if not request.user.has_perm('blogposts.change_blogpost'):
        #     return redirect(reverse('blogs:index'))
        return super().dispatch(request, *args, **kwargs)


class PostUpdateView(PostOwnerPermissionMixin, UserPassesTestMixin, UpdateView):

    raise_exception = False
    permission_required = 'posts.change_post'
    permission_denied_message = ''

    template_name = 'blogapp/post_create.html'
    fields = ['title', 'content']
    model = Post

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user.profile


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blogs:index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user.profile


@login_required
def like(request, post_id):
    if request.method == 'POST':
        try:
            like = Like.objects.get(
                liker=request.user.profile, post_id=post_id)
            like.active = not like.active
        except Like.DoesNotExist:
            like = Like(liker=request.user.profile,
                        post_id=post_id, active=True)
        like.save()

    return redirect(reverse('blogs:post-detail', kwargs={'pk': post_id}))
