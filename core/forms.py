# -*- coding: utf-8 -*-
from django import forms
STATUS_CHOICES = ( ('Only Me', 'Only Me'), ('Public', 'Public'),('Community', 'Community'),) 
class DocumentForm(forms.Form):
	docfile = forms.FileField(label='Select a file',)
 	select = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))

print DocumentForm().as_p() 	