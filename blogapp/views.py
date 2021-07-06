from django.views.generic import ListView, CreateView

from .models import Post
from blogauth.models import BlogProfile
from .forms import PostCreateForm
# Create your views here.


class PostListView(ListView):
    template_name = 'blogapp/index.html'
    model = Post
    paginate_by = 10


class PostCreateView(CreateView):
    template_name = 'blogapp/post_create.html'
    form_class = PostCreateForm
    success_url = '/blogs/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        profile = BlogProfile.objects.filter(user=self.request.user)
        kwargs.update({'author': profile})
        return kwargs
