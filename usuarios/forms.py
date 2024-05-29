from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Usuario
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField  # Corrected import
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class UsuarioEditForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'cpf', 'telefone', 'data_nascimento']


class UsuarioForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "username"}))
    password = forms.PasswordInput(attrs={"class": "password"})
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "email"}))
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={"class": "data_nascimento"}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={"class": "cpf"}))
    telefone = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget(attrs={'class': 'telefone'}))

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'email', 'cpf', 'telefone', 'data_nascimento']  # Incluindo campos adicionais

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de Usuário'
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError('Endereço de email inválido.')
        return email

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if len(cpf) != 11:
            raise forms.ValidationError('CPF deve ter 11 dígitos.')
        if Usuario.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Este CPF já está em uso.')
        return cpf
 

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if len(telefone) < 8:
            raise forms.ValidationError('Telefone deve ter no mínimo 8 dígitos.')
        return telefone

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError('Nome de usuário deve ter no mínimo 3 caracteres.')
        return username