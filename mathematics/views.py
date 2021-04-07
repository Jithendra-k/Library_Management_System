from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Maths
from .forms import MathematicsForm
from django.contrib import messages
# Create your views here.


def mathematics(request):
    return render(request, 'mathematics/view-mathematics.html', {'mlist': Maths.objects.all()})


@login_required
def add_mathematics(request):
    if request.method == 'POST':
        form = MathematicsForm(request.POST)
        if form.is_valid():
            form.save()
            m_name = form.cleaned_data.get('m_name')
            messages.success(request, f'New Book {m_name} added in LMS!')
            return redirect('add-mathematics')
    else:
        form = MathematicsForm()
    return render(request, 'mathematics/add-mathematics.html', {'form': form})
