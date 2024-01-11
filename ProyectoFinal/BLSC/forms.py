from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from django import forms

class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {k: "" for k in fields}