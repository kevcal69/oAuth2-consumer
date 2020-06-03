from django.contrib.auth.views import LoginView


class HomePage(LoginView):
    template_name = 'account/login.html'
