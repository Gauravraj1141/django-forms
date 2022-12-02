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


class MyForm(forms.Form):
    MyName = forms.CharField()

    def clean_MyName(self):
        valname = self.cleaned_data["MyName"]
        if len(valname) < 4:
            raise forms.ValidationError("Please Enter greater than 4 values")

        return valname


form = MyForm()
