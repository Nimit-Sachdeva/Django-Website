from django import forms

class FormName(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(widget=forms.Textarea,required=True)
    # botcatcher= forms
