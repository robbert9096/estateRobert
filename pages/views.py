from django.shortcuts import  render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices,state_choices
# Create your views here.


def home(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings' : listings,
        'state_choices' : state_choices,
        'price_choices' : price_choices,
        'bedroom_choices' : bedroom_choices,
    }
    return render(request, "pages/home.html", context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    seller_of_the_month = Realtor.objects.all().filter(is_mvp=True)
    return render(request, "pages/about.html",{
        "mvp": seller_of_the_month,
        "realtors" : realtors
    }) 