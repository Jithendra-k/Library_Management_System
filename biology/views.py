from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BiologyForm
from .models import Biology

def biology(request):
    return render(request, 'biology/view-biology.html',{'blist': Biology.objects.all()})


@login_required
def add_biology(request):
    if request.method == 'POST':
        form = BiologyForm(request.POST)
        if form.is_valid():
            form.save()
            b_name = form.cleaned_data.get('b_name')
            messages.success(request, f'New Book {b_name} added in LMS!')
            return redirect('add-biology')
    else:
        form = BiologyForm()
    return render(request, 'biology/add-biology.html', {'form': form})