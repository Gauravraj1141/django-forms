from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Registrationform
# Create your views here.


def success(request):
    return render(request, "formapp/success.html")


def home(request):
    if request.method == "POST":
        fmdata = Registrationform(request.POST)
        if fmdata.is_valid():
            print("validate")
            print(fmdata.cleaned_data)
            print(fmdata.cleaned_data["Name"])
            print(fmdata.cleaned_data["Email"])
            print(fmdata.cleaned_data["Phone"])
            print(fmdata.cleaned_data["division"])
            return HttpResponseRedirect("/success")
    else:
        fm = Registrationform()
    return render(request, 'formapp/form.html', {"fms": fm})
