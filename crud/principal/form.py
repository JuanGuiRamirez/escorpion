from django import forms
from principal.models import producto

class ProductoForm(forms.ModelForm):
	class Meta:
		model = producto