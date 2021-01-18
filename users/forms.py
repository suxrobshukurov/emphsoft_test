from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserOurRegistraion(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"}),
        required='')
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"}),
        required='')
    father_name = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(
            attrs={
                "class": "form-control"}),
        required='')
    bio = forms.CharField(
        label='О себе',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 5}),
        required='')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'father_name', 'bio']


class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ['img']
