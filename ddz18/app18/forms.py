from django import forms
from app18.models import Book, Author
class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['slug']

class CreateAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"