from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	firstname=forms.CharField(required=True)
	lastname=forms.CharField(required=True)
	class Meta:
		model = User
		fields = ("username", "email","firstname","lastname", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.firstname=self.cleaned_data['firstname']
		user.lastname=self.cleaned_data['lastname']
		# user.password1=self.cleaned_data['password1']
		# user.password2=self.cleaned_data['password2']
		if commit:
			user.save()
		return user