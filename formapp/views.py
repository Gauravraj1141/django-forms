from django.shortcuts import render
from .forms import Registrationform
# Create your views here.


def home(request):
    fm = Registrationform()

    return render(request, 'formapp/form.html', {"fms": fm})
