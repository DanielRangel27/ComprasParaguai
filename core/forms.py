from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm as AllauthSignupForm
from allauth.socialaccount.models import SocialAccount

from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(AllauthSignupForm):
    def __init__(self, *args, **kwargs):
        sociallogin = kwargs.pop("sociallogin", None)
        super().__init__(*args, **kwargs)
        self.fields['google_login'] = forms.BooleanField(required=False, widget=forms.HiddenInput)
        self.fields['facebook_login'] = forms.BooleanField(required=False, widget=forms.HiddenInput)
        self.fields['username'].widget.attrs.update({
            'class': '',
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'John Doe',
            'maxlength': '16',
            'minlength': '6',
        })
        self.fields['email'].widget.attrs.update({
            'class': '',
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'JohnDoe@mail.com',
        })
        self.fields['password1'].widget.attrs.update({
            'class': '',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': 'Senha',
            'maxlength': '22',
            'minlength': '8'
        })
        self.fields['password2'].widget.attrs.update({
            'class': '',
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': 'Confirmar',
            'maxlength': '22',
            'minlength': '8'
        })
        if sociallogin:
            self.fields['google_login'].initial = sociallogin.account.provider == 'google'
            self.fields['facebook_login'].initial = sociallogin.account.provider == 'facebook'
            self.fields['email'].widget = forms.HiddenInput()
            self.fields['email'].required = False

    def save(self, request):
        user = super().save(request)
        if self.cleaned_data.get('google_login'):
            # Lógica de autenticação com o Google
            # Por exemplo, verifique se o usuário possui uma conta associada ao Google
            if SocialAccount.objects.filter(user=user, provider='google').exists():
                # Autenticação bem-sucedida com o Google
                pass
            else:
                # Falha na autenticação com o Google
                pass
        elif self.cleaned_data.get('facebook_login'):
            # Lógica de autenticação com o Facebook
            # Por exemplo, verifique se o usuário possui uma conta associada ao Facebook
            if SocialAccount.objects.filter(user=user, provider='facebook').exists():
                # Autenticação bem-sucedida com o Facebook
                pass
            else:
                # Falha na autenticação com o Facebook
                pass
        return user
    username = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'google_login', 'facebook_login',)
