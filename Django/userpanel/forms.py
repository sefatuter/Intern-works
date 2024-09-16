from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from userpanel.models import Todo


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text', 'completed']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your todo'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
