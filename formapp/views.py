from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Registrationform, MyForm
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


def secondForm(request):
    if request.method == "POST":
        myfmdata = MyForm(request.POST)
        if myfmdata.is_valid():
            print("validate")
            print(myfmdata.cleaned_data)
            myfm = MyForm()
    else:
        myfm = MyForm()
    return render(request, "formapp/newform.html", {'newfm': myfm})
