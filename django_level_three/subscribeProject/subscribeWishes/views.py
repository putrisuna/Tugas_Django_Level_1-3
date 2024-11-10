from django.shortcuts import render
from subscribeWishes.models import Customer
from subscribeWishes.forms import NewSubscriber
# Create your views here.
def index(request):
    return render(request, 'subscription/index.html')

def customer(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers' :customer_list}
    return render(request, 'subscription/customers.html', context=customer_dict)

def subscribe(request):
    form = NewSubscriber()

    if request.method == "POST":
        form = NewSubscriber(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return customer(request)
        else:
            print("Error: Form invalid")

    return render (request, 'subscription/subscribe.html', {'form':form})