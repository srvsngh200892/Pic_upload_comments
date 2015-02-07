from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class TaskForm(forms.Form):
 
    title = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("title"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    created_date = forms.DateTimeField(widget=forms.TextInput(attrs=dict(required=False, max_length=30)), label=_("created_date"))
    priority = forms.IntegerField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("priority"))
    visibilty = forms.IntegerField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("visibilty"))
    status = forms.IntegerField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("status"))
 