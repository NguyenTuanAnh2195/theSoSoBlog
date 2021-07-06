from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.views import LoginView


from .models import BlogProfile
from .forms import UserRegisterForm


class ProfileRegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = '/accounts/'
    template_name = 'blogauth/register.html'


class ProfileLoginView(LoginView):
    pass


class BlogProfileDetailView(DetailView):
    model = BlogProfile


class BlogProfileListView(ListView):
    model = BlogProfile
    paginate_by = 10
