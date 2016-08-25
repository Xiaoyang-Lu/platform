from django import forms

from models import Matrix


class MatrixForm(forms.Form):
	FILESYS_CHOICES = (
		('filesys1', 'filesys1'),
		('filesys2', 'filesys2'),
		('filesys3', 'filesys3'),)
	filesys = forms.MultipleChoiceField(choices = FILESYS_CHOICES,
								 		widget = forms.CheckboxSelectMultiple(),
								 		initial = ['filesys1'],
								 		required = True,
								 		label = 'File system')

	def clean_filesys(self):
		filesys = self.cleaned_data.get('filesys')
		if not filesys:
			raise forms.ValidationError('One File System Must Be Chosen')
		return filesys

	MX_CHOICES = (
		('mx1', 'mx1'),
		('mx2', 'mx2'),
		('mx3', 'mx3'),
		('mx4', 'mx4'),)
	matrix = forms.ChoiceField(choices = MX_CHOICES, 
								required = True, 
								label = 'Matrix')