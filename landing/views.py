from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, ListView

from .models import Enterprise, Request


# Create your views here.


def home(request):
    if request.method == "POST":
        Request.objects.create(
            name=request.POST['name'],
            name_enterprise=request.POST['name_enterprise'],
            email=request.POST['email'],
            phone=request.POST['phone'],
        )
        return redirect("landing:success_request")
    return render(request, 'core/home.html', {'enterprises': Enterprise.objects.all()})


class EnterpriseDetailView(DetailView):
    model = Enterprise
    context_object_name = 'enterprise'
    template_name = 'core/enterprise_detail.html'


class EnterpriseListView(ListView):
    model = Enterprise
    context_object_name = 'enterprises'
    template_name = 'core/enterprise_list.html'
    paginate_by = 10

def success_request(request):
    return render(request, 'core/success_request.html')

def store(request):
    return render(request, 'core/store.html')

