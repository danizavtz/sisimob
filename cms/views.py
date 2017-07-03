# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .forms import AuthenticateForm, ImovelCadastro
from .models import Imovel

def home(request,auth_form=None):
    if request.user.is_authenticated():
        user = request.user
        return render(request, "rent/home.html",{'user':user,  'next_url': '/'})
    else:
        auth_form = auth_form or AuthenticateForm()
        return render(request, "rent/index.html",{'auth_form': auth_form})

@login_required
def cadastro(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

@login_required
def new(request):
	return render(request, 'rent/cadastro_form.html', {'form': ImovelCadastro()})


@login_required
def create(request):
	form = ImovelCadastro(request.POST)
	if not form.is_valid():
		return render(request, 'rent/cadastro_form.html', {'form': form})
	obj = form.save(commit=False)
	obj.save()
	return HttpResponseRedirect('/cadastro/%d' % obj.pk)


@login_required
def detail(request,pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    context = {'imovel': imovel}
    return render(request, 'rent/detail.html', context)

def logout_view(request):
	logout(request)
	return redirect('/')

def login_view(request):
	if request.method == 'POST':
		login_post(request)
	return redirect('/')

def login_post(request):
	form = AuthenticateForm(data=request.POST)
	if not form.is_valid():
		return render(request, 'rent/home.html', {'form': form})
	login(request, form.get_user())
	return redirect('/')

def imoveis_view(request):
    imoveis = Imovel.objects.all()
    context = {'imoveis': imoveis }
    return render(request, 'rent/listview.html',context)