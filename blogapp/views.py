from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import (
    ListView, CreateView, DetailView, DeleteView
)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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


class PostCreateView(CreateView, LoginRequiredMixin):
    template_name = 'blogapp/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('blogs:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        profile = self.request.user.profile
        kwargs.update({'author': profile})
        return kwargs


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('blogs:index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user.profile:
            messages.add_message(request, messages.ERROR,
                                 'You do not have the right to delete this post')
            return redirect(
                reverse('blogs:post-detail', kwargs={'pk': self.object.id})
            )
        return super().post(request, *args, **kwargs)


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
