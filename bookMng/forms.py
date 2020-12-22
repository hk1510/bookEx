from django import forms
from django.forms import ModelForm
from .models import Book
from.models import Review

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            "description",
        ]
        widgets = {
            "description": forms.Textarea(attrs={'cols':80}),
        }
        labels = {
            "description": ''
        }

