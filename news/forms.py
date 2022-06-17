from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
    MY_CHOICES = (
        ('a', 'Политика'),
        ('b', 'Культура'),
        ('c', 'Авто'),
        ('d', 'Спорт'),
    )
    #post_category = forms.CharField(min_length=2, max_length=32)
    post_category = forms.ChoiceField(choices=MY_CHOICES)
    #post_category = forms.ChoiceField(choices=Post.post_category.name)
    title = forms.CharField(max_length=128)
    #text = forms.TextField(min_length=10)

    class Meta:
        model = Post
        fields = [
            #'datetime',
            'post_category',
            'title',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        post_category = cleaned_data.get("post_category")
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        # if name == description:
        #     raise ValidationError(
        #         "Описание не должно быть идентично названию."
        #     )

        return cleaned_data