from django.contrib.auth.forms import UserCreationForm, UserModel
from django import forms
from django.contrib.auth.password_validation import MinimumLengthValidator

class NoMinimumLengthValidator(MinimumLengthValidator):
    def __init__(self, min_length=8):
        super().__init__(min_length)

    def validate(self, password, user=None):
        pass

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=20, label='Usuarix', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}), validators=[NoMinimumLengthValidator()])
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Desactiva la verificación de contraseñas comunes
        self.fields['password1'].validators = []  # Esto desactiva la verificación de contraseñas comunes

    class Meta:
        model = UserModel
        fields = ["email", "username", "password1", "password2"]
        help_texts = {k: "" for k in fields}




class UserEditionFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}