from django.shortcuts import render
from django.template import loader
from .models import Ad, User, Category, Address, Conversation, Message, Mission
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import AdForm


def home(request):
    template = loader.get_template('home.html')
    context = {
        'text': 'Hello World'
    }

    return HttpResponse(template.render(context, request))


def users(request):
    template = loader.get_template('user/user.html')
    context = {
        'users': User.objects.all
    }

    return HttpResponse(template.render(context, request))


def ad_list(request):
    template = loader.get_template('ad/list.html')
    context = {
        'ads': Ad.objects.all
    }

    return HttpResponse(template.render(context, request))


def ad_supply(request):
    template = loader.get_template('ad/supply.html')
    context = {
        'ads': Ad.objects.filter(type='supply')
    }

    return HttpResponse(template.render(context, request))


def ad_demand(request):
    template = loader.get_template('ad/demand.html')
    context = {
        'ads': Ad.objects.filter(type='demand')
    }

    return HttpResponse(template.render(context, request))


def ad_details(request, id):
    template = loader.get_template('ad/details.html')
    id_ad = int(id)
    context = {
        'ad': Ad.objects.get(id=id_ad)
    }

    return HttpResponse(template.render(context, request))


def ad_add(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('worker:ad_list'))
    else:
        form = AdForm()

    return render(request, 'ad/form/add.html', {'form': form})