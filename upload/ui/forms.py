#coding:utf8
from django import forms

class OemResourcesForm(forms.Form):
    filename = forms.FileField(label=u'升级包')
