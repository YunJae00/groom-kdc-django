from django import forms


class SimpleUploadForm(forms.Form):

    title = forms.CharField(max_length=50)

    # ImageField Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
    # file = forms.FileField()
    # imagefield 는 filefield를 더 발전시킨 필드
    image = forms.ImageField()