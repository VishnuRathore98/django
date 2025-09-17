from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

def hello_world(request):
    return HttpResponse("Hello from func")

class Hello(View):
    def get(self, request):
        return HttpResponse("Hello from class")

def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")

    return render(request, 'index.html', {'form':form})
