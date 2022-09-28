from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm

# Create your views here.

class Register(View):
    template_name = 'auth/register.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class
        
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        

        return render(request, self.template_name, {'form':form})


