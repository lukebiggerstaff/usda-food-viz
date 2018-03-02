from django import forms


class Search(forms.Form):
    query = forms.CharField()
