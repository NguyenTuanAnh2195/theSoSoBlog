from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import BlogProfile
from .forms import UserRegisterForm


class ProfileRegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = '/accounts/'
    template_name = 'blogauth/register.html'


class ProfileLoginView(views.LoginView):
    pass


class ProfileLogoutView(views.LogoutView):
    pass


class BlogProfileDetailView(DetailView):
    model = BlogProfile


class BlogProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'blogauth/blogprofile_update.html'
    fields = ['first_name', 'last_name', 'username', 'email']

    def get_success_url(self) -> str:
        return reverse_lazy(
            'accounts:user-detail', kwargs={'pk': self.object.id}
        )

    def get(self, request, *args, **kwargs):
        if args.pk != self.user.id:
            return reverse_lazy(
                'accounts:user-detail', kwargs={'pk': self.object.id}
            )
        super().get(request, *args, **kwargs)


class BlogProfileListView(LoginRequiredMixin, ListView):
    model = BlogProfile
    paginate_by = 10
