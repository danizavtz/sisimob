from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Imovel
from django import forms
from django.utils.html import strip_tags

class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'usuário'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder':'senha'}))

    def is_valid(self):
        form = super(AuthenticateForm,self).is_valid()
        for f, error in self.errors.items():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

class ImovelCadastro(forms.ModelForm):
	class Meta:
		model = Imovel
		fields = '__all__'