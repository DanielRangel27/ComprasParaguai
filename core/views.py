from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

class IndexView(TemplateView):
    template_name = 'index.html'
class MyLoginView(LoginView):
    def form_invalid(self, form):
        # Adicione sua mensagem de erro aqui
        messages.error(self.request, 'Usuário ou senha inválidos.')
        return super().form_invalid(form)

def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(request)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    return render(request, 'registro.html', {'form': form})
