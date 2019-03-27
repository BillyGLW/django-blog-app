from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = None


class LoginForm(forms.Form):
	post = forms.CharField(max_length = 100)
	post_title = forms.CharField(max_length = 100)
	post_description = forms.CharField(max_length = 100, widget = forms.Textarea)
	ppost_date = forms.DateField()

class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=30, required=False, help_text='Prioritize.')
    content = forms.CharField(max_length=30, required=False, help_text='Prioritize.')
    created_date = forms.CharField(max_length=30, required=False, help_text='Prioritize.')
    article_image = forms.CharField(max_length=30, required=False, help_text='Prioritize.')
