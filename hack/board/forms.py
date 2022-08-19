from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    content = forms.CharField(
		widget=forms.Textarea(attrs={'style':"width:1270px;height:100px;font-size:17px;border:1px solid black;background-color: d1d7d5; margin-left:10%;",  'placeholder':"댓글을 입력하세요!",'border': '3px solid black;','background-color': '#f5d682;'}),
		label=''
	)
    class Meta:
        model = Comment
        fields = ('content',)


