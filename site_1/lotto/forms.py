from django import forms
from .models import GuessNumbers


class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        # 어떤 값들을 user 한테 입력 받을 것인가 * 문자열로 적어줘야함
        fields = ('name', 'text',)
