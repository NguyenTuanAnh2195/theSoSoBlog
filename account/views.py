from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
# from django.contrib.auth import authenticate

from account.forms import UserForm
from account.models import User


class SignupView(FormView):
    template_name = 'account/signup.html'
    form_class = UserForm
    success_url = reverse_lazy('account:index')

    def form_valid(self, form):
        user = form.save(False)
        user.set_password(user.password)
        user.save()
        super().form_valid(self, form)


class UserListView(ListView):
    model = User
    paginate_by = 20
    template_name = 'account/account_list.html'
