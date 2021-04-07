from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import OOPS
from .forms import OOPSForm
from django.contrib import messages
# Create your views here.


def oops(request):
    return render(request, 'oops/view-oops.html', {'olist': OOPS.objects.all()})


@login_required
def add_oops(request):
    if request.method == 'POST':
        form = OOPSForm(request.POST)
        if form.is_valid():
            form.save()
            o_name = form.cleaned_data.get('o_name')
            messages.success(request, f'New Book {o_name} added in LMS!')
            return redirect('add-oops')
    else:
        form = OOPSForm()
    return render(request, 'oops/add-oops.html', {'form': form})