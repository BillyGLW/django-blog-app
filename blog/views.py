from django.contrib.auth import get_user_model
MyUser = get_user_model()
import json
from django.http import JsonResponse
# django auth decorator for login
from django.contrib.auth.decorators import login_required
# 404 error raise
from django.http import Http404

from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.models import BlogCPosts, BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views import generic
from rest_framework import generics
from blog.forms import LoginForm, SignUpForm, BlogPostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.db import models
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from django.http import HttpResponseRedirect
import datetime
from django.utils.datastructures import MultiValueDictKeyError
# printing request in a string format ;)
from django.utils.html import escape

def index(request):
	c = {}
	c.update(csrf(request))
	all_posts = BlogCPosts.objects.all()

	current_user = request.user

	context = {'all_posts': all_posts, 'current_user': current_user}
	response = render(request, 'main.html', context)
	return response
def personal_blog(request):
	if request.user.is_authenticated:
		try:
			article = BlogPost.objects.all()
		except:
			return HttpResponseRedirect(reverse("blog:error404"))
		current_user = request.user
		context = {'all_posts': article, 'current_user': current_user}
		response = render(request, 'blog.html', context)
		return response
	else:
		return HttpResponseRedirect(reverse("blog:error404"))
def User_Logout(request):
	try:
		logout(request)
		return HttpResponseRedirect(reverse("blog:index"))
	except: 
		return HttpResponseRedirect(reverse("blog:error404"))
def error404(request):
	raise Http404
def contact_blog(request):
	c = {}
	c.update(csrf(request))
	all_posts = BlogCPosts.objects.all()
	current_user = request.user
	context = {'all_posts': all_posts, 'current_user': current_user}
	response = render(request, 'contact.html', context)
	return response

#  Pretty Request: https://gist.github.com/defrex/6140951
def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )
# Zyhu: Json Request
def register_new_user(request):
	c = {}
	c.update(csrf(request))
	username = request.POST['username']
	password = request.POST['password']
	newuser = MyUser(email = username)
	newuser.set_password(password)
	newuser.save()
	data = {
        'is_taken': MyUser.objects.filter(email__iexact=username).exists(),
        'debug_info': escape(repr(request)),
        'username': username, 
    }

	pretty = pretty_request(request)
	return HttpResponse(pretty)
	
# Zyhu: Json Request
def login_user(request):
	c = {}
	c.update(csrf(request))
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
	pretty = pretty_request(request)
	return HttpResponse(pretty)

def post_new(request):
 	c = {}
 	c.update(csrf(request))
 	if (request.method == 'POST'):
 		form1 = request.POST.get('title')
 		form2 = request.POST.get('content')
 		form3 = request.POST.get('created_date')
 		form4 = request.POST.get('article_image')
 	blogpost = BlogPost.objects.create(author_id = request.user.id, title = form1, content = form2, article_image = form4)
 	blogpost.save()
 	return HttpResponseRedirect(reverse("blog:personal_blog"))
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
	else:
		form = UserCreationForm()

	context = {'form': form}
	return render(request, 'registration/register.html', context)

class Blog_Posting(FormView):
	model = BlogPost
	user = ''
	form_class = BlogPostForm
	template_name = 'panel.html'

	def form_valid(self, form):
		self.user = ''
		super(Blog_Posting, self).form_valid(form) 	

		return render(self.request, self.template_name, self.get_context_data(form=form)) 
	def get_context_data(self, **kwargs):
		context = super(Blog_Posting, self).get_context_data(**kwargs)
		context['current_user'] = self.request.user
		return context
