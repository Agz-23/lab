from django import forms
from Order.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'rating']
        

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
     