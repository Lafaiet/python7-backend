from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    birth_day = forms.DateField(widget=forms.SelectDateWidget, required=False, label='Date of Birth')
    message = forms.CharField(max_length=500, widget=forms.Textarea)