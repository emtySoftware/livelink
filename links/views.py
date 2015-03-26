from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.contrib.auth
from links.forms import LoginForm
from links import forms as lforms
from links import models as lmodels
# Create your views here.

class Login(View):

	def get(self, request):
		form = LoginForm()
		return render(request, 'login.html', locals())

	def post(self, request):
		form = LoginForm(request.POST)
		error = None

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				return redirect('/')
			else:
				error = 'Usuario no existe'

		return render(request, 'login.html', locals())


class Registration(View):

	def get(self, request):
		form = UserCreationForm()
		return render(request, 'registration.html', locals())

	def post(self, request):
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/')

		return render(request, 'registration.html', locals())

	def dispatch(self, request, **kwargs):
		if request.user.is_authenticated():
			return redirect('/')

		return super(Registration, self).dispatch(request, *args, **kwargs)

class NewLink(View):

	def get(self, request):
		form = lforms.LinkForm()
		return render(request, 'newlink.html', locals())

	def post(self, request):
		form = lforms.LinkForm(request.POST)
		if form.is_valid():
			form.save(user=request.user)
			return redirect(reverse('links'))
		return render(request, 'newlink.html', locals())

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(NewLink, self).dispatch(request, *args, **kwargs)

class Link(View):
	def get(self, request):
		user = request.user
		mlinks = lmodels.Link.objects.filter(user=request.user)
		olinks = lmodels.Link.objects.exclude(user=request.user)

		return render(request, 'links.html', locals())

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(Link, self).dispatch(request, *args, **kwargs)


@login_required
def add_fav(request, id):
	link = get_object_or_404(lmodels.Link, id=id)

	if link.user.pk == request.user.pk:
		return ('/')

	request.user.links.add(link)
	request.user.save()

	return redirect('/links')

@login_required
def rm_fav(request, id):
	link = get_object_or_404(lmodels.Link, id=id)

	request.user.links.remove(link)
	request.user.save()

	return redirect('/links')

def logout(request):
	auth_logout(request)
	return redirect('/')