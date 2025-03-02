from django import forms

from avtoapp.models import Car_s


# class CarForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Malumot',
#                             widget=forms.TextInput(attrs={'class': 'form-control'}))
#     context = forms.CharField(label='Text', required=False, widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'rows': 5,
#     }))
#     color= forms.BooleanField(label='Is Bool',initial=True)
#     car= forms.ModelChoiceField(empty_label="bir nima",label='car',queryset=Car_s.objects.all(),
#                                 widget=forms.Select(attrs={'class': 'form-control'}))

class CarForm(forms.ModelForm):
    class Meta:
        model = Car_s
        # fields = '__all__'
        fields = ['title', 'brand','color','price', 'image', 'context']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'context': forms.Textarea(attrs={'class': 'form-control'}),

        }

    # def clean(self):
    #     title = self.cleaned_data.get('title')
    #     if re.