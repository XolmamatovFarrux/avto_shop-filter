from django import forms

from avtoapp.models import Car_s


class CarForm(forms.Form):
    title = forms.CharField(max_length=150, label='Malumot',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    context = forms.CharField(label='Text', required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
    }))
    color= forms.BooleanField(label='Is Bool',initial=True)
    car= forms.ModelChoiceField(empty_label="bir nima",label='car',queryset=Car_s.objects.all(),
                                widget=forms.Select(attrs={'class': 'form-control'}))