from django import forms

from .models import Manager

class manager_manage_form(forms.ModelForm):

    class Meta:
        model = Manager
        fields = ('id', 'pw', 'pos', 'phonenum')
