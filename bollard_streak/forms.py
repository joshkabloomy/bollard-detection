from django import forms

class CheckCountry(forms.Form):
    word_to_check = forms.CharField(max_length=100, label="Enter a country")
