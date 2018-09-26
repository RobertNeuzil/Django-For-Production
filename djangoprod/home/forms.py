from django import forms

class EntryForm(forms.Form):
	author = forms.CharField(max_length=40,
		widget=forms.TextInput(
			attrs={
			
			'class': '',
}))
	date = forms.CharField(max_length=40,
		widget = forms.TextInput(
			attrs={

			'class': 'form-control'




			}))
	message = forms.CharField(max_length=200,
		widget = forms.TextInput(
			attrs={

			'class': ''





			}))