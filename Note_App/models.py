from django.db import models
from django import forms


# Create your models here.

class Notes_Form(forms.Form):
    title = forms.CharField(label="Title", max_length=255, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                         "placeholder": "Title"}))
    note = forms.CharField(label="Note", widget=forms.Textarea(attrs={"class": "form-control",
                                                                      "placeholder": "Note"}), required=False)


class Notes_Update(forms.Form):
    title = forms.CharField(label="Title", max_length=255, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                         "placeholder": "Title"}))
    note = forms.CharField(label="Note", widget=forms.Textarea(attrs={"class": "form-control",
                                                                      "placeholder": "Note"}), required=False)


class Notes_Record(models.Model):
    title = models.CharField(max_length=255)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
