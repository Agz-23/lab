from django.shortcuts import render, get_object_or_404, redirect
from Order.models import Shoe, Brand, Comment, Order, Customer
from Order.forms import CommentForm  
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home.html')

class BrandListView(ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brand'

class ShoeListView(ListView):
    model = Shoe
    template_name = 'shoe_list.html'
    context_object_name = 'shoes'
    paginate_by = 10

class ShoeDetailView(DetailView):
    model = Shoe
    template_name = 'shoe_detail.html'
    context_object_name = 'shoe'

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

    def form_valid(self, form):
        form.instance.product = get_object_or_404(Shoe, id=self.kwargs['shoe_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('shoe-detail', kwargs={'pk': self.kwargs['shoe_id']})
        
class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'