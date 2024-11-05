# shapes/forms.py

from django import forms

class ShapeCodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea, label="Python Code", help_text="Define a shape class inheriting from Shape.")
