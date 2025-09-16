from django import forms


class BookingForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    phone = forms.CharField(max_length=50, required=False)
    event_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    event_type = forms.CharField(max_length=120)
    message = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


