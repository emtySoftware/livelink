from django import forms
from .models import Link, User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='Confirm password')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1', None)
        password2 = self.cleaned_data.get('password2', None)

        print password1, password2
        if (password1 and password2 and password1 != password2) or (not password1 or not password2):
            raise forms.ValidationError('Password mismatch')

        return password1

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        fields = ('username', )
        model = User

class LinkForm(forms.ModelForm):

    def save(self, user=None, *args, **kwargs):
        self.instance.user = user
        super(LinkForm, self).save(**kwargs)

    class Meta:
        model = Link
        fields = ('url', )
