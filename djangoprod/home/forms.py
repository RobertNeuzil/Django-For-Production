from django import forms

class EntryForm(forms.Form):
	author = forms.CharField(max_length=40,
		widget=forms.TextInput(
			attrs={

			'class': 'form-control',
			'placeholder': 'Author',
			'id': 'Author',
			'required data-validation-required-message': 'Please enter your name.',}))
	date = forms.CharField(max_length=40,
		widget = forms.TextInput(
			attrs={

			'class': 'form-control',
			'placeholder': 'Date',
			'id': 'Date',
			'required data-validation-required-message': 'Please enter a date address.',



			}))
	message = forms.CharField(max_length=200,
		widget = forms.TextInput(
			attrs={
			
			'class': 'form-control',
			'placeholder': 'message',
			'id': 'message',
			'required data-validation-required-message': 'Please enter a Message',



			}))