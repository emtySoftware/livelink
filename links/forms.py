from django import forms
from .models import Link


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class LinkForm(forms.ModelForm):

    def save(self, user=None, *args, **kwargs):
        self.instance.user = user
        super(LinkForm, self).save(**kwargs)

    class Meta:
        model = Link
        fields = ('url', )
