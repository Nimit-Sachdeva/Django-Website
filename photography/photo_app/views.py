from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.
def index(request):
    return render(request,'photo_app/index.html',)

def form_name_view(request):
    form = forms.FormName()
    if request.method== "POST":
        form=forms.FormName(request.POST)
        if form.is_valid():
            print ("Validation Successful")
            print("NAME: "+ form.cleaned_data['name'])
            print("EMAIL: "+ form.cleaned_data['name'])
            print("TEXT: "+ form.cleaned_data['name'])
    return render(request,'photo_app/form.html',{'form':form})
    
