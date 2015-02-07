from django.db import models
from django import forms
from dbarray import IntegerArrayField

from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = ( 

  ('Only Me', 'Only Me'), 

  ('Public', 'Public'),

  ('Community', 'Community'),

) 

class Image(models.Model):
    user = models.ForeignKey(User)
    imagefile = models.ImageField(upload_to='myapp/pics/%Y/%m/%d')
    status  = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Only Me')
    created_date = models.DateField(auto_now=True, auto_now_add=True)
    modified_date = models.DateField(auto_now=True, auto_now_add=True)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, default = None)
    image = models.ForeignKey(Image, null=True, blank=True, default = None)
    date = models.DateTimeField(auto_now_add=True)
    path = IntegerArrayField(blank=True, editable=False)
    depth = models.PositiveSmallIntegerField(default=0)
    created_date = models.DateField(auto_now=True, auto_now_add=True)
    modified_date = models.DateField(auto_now=True, auto_now_add=True)
    
    def __unicode__(self):
        return self.content
    
class CommentForm(forms.ModelForm):
    #Hidden value to get a child's parent
    parent = forms.CharField(widget=forms.HiddenInput(
                            attrs={'class': 'parent'}), required=False)
    
    class Meta:
        model = Comment
        fields = ('content',)