from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import Profile


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # Had to use the constructor because password inputs wouldn't render bootstrap normally.
        self.fields['password1'].widget.attrs = {
            'class': 'form-control',
            'id': 'password1Input',
            'placeholder': 'Introduzca su contraseña',
            'required': 'required'}
        self.fields['password2'].widget.attrs = {
            'class': 'form-control',
            'id': 'password2Input',
            'placeholder': 'Confirme su contraseña',
            'required': 'required'}

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'password1', 'password2']
        # This adds a bootstrap class to django's fields as an attribute.
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'userNameInput',
                    'aria-describedby': 'userNameHelp',
                    'placeholder': 'Introduzca su nombre de usuario',
                    'required': 'required',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'firstNameInput',
                    'placeholder': 'Introduzca su nombre',
                    'required': 'required',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'lastNameInput',
                    'placeholder': 'Introduzca su apellido',
                    'required': 'required',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'emailInput',
                    'aria-describedby': 'emailHelp',
                    'placeholder': 'Introduzca su correo electrónico',
                    'required': 'required',
                }
            )
        }


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email']
        # This adds a bootstrap class to django's fields as an attribute.
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control mt-1',
                    'id': 'userNameInput',
                    'aria-describedby': 'userNameHelp',
                    'placeholder': 'Introduzca su nombre de usuario',
                    'required': 'required',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control mt-1',
                    'id': 'firstNameInput',
                    'placeholder': 'Introduzca su nombre',
                    'required': 'required',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control mt-1',
                    'id': 'lastNameInput',
                    'placeholder': 'Introduzca su apellido',
                    'required': 'required',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control mt-1',
                    'id': 'emailInput',
                    'aria-describedby': 'emailHelp',
                    'placeholder': 'Introduzca su correo electrónico',
                    'required': 'required',
                }
            )
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
