from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm, FilterListView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

# Create your views here.

class CustomerList(ListView):
    model = Customer
    template_name = 'crud/index.html'
    context_object_name = 'customers'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form List View'
        context['filter_form'] = FilterListView(self.request.GET)
        get_copy = self.request.GET.copy()
        if get_copy.get('page'):
            get_copy.pop('page')
        context['get_copy'] = get_copy
        return context

    def get_queryset(self):
        queryset = Customer.objects.all().order_by('-id')
        name = self.request.GET.get('name')
        print(name)
        if name:
            queryset = queryset.filter(name__icontains=name)
        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = queryset.order_by(order_by)
        return queryset


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'crud/detail.html'
    context_object_name = 'customer'


class CustomerCreate(FormView):
    model = Customer
    template_name = 'crud/create.html'
    form_class = CustomerForm
    success_url = '/cb/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form): 
        return super().form_invalid(form)

class CustomerUpdate(UpdateView):
    model = Customer
    template_name = 'crud/update.html'
    fields = ['name', 'email', 'phone']
    success_url = '/cb/'

class CustomerDelete(DeleteView):
    model = Customer
    success_url = '/cb/'

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

    
def get_users(request):
    print('function base index')
    customer_obj = Customer.objects.all()
    return render(request, 'crud/index.html', {'customers': customer_obj})

def get_user(request, pk):
    print('function base detail')
    customer_obj = Customer.objects.get(id=pk)
    return render(request, 'crud/detail.html', {'customer': customer_obj})

def create_user(request):
    print('function base create')
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cb/')
    else:
        form = CustomerForm()
    return render(request, 'crud/create.html', {'form': form})

def update_user(request, pk):
    print('function base update')
    customer_obj = Customer.objects.get(id=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer_obj)
        if form.is_valid():
            form.save()
            return redirect('/cb/')
    else:
        form = CustomerForm(instance=customer_obj)
    return render(request, 'crud/update.html', {'form': form})