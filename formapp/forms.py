from django import forms


class Registrationform(forms.Form):
    Name = forms.CharField(max_length=100, label_suffix=" - ", widget=forms.TextInput(
        attrs={"placeholder": "Enter Yur Name"}))
    Email = forms.EmailField(label_suffix=" - ", widget=forms.TextInput(
        attrs={"placeholder": "Enter Your Email"}))
    Phone = forms.IntegerField(label_suffix=" - ", widget=forms.TextInput(
        attrs={"placeholder": "Enter Phone Number"}))
    division = forms.CharField(label_suffix=" - ", label="Class", max_length=100, widget=forms.TextInput(
        attrs={"placeholder": "Class Name  .."}))
