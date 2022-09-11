from webbrowser import get
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Listing
from django.views.generic import TemplateView
from .choices import price_choices, bedroom_choices,state_choices 
# Create your views here.


def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listing,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request, "listings/listings.html", {
        'listing' : paged_listings
    })

class SingleListingView(TemplateView):
    template_name = "listings/listing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_id = kwargs['listing_id']
        selected_listing = Listing.objects.get(pk=get_id)
        context["listing"] = selected_listing 
        return context
    
    

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
# Keywords     
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

# City 
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

# State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

# Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

# Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)


    context = {
        'price_choices' : price_choices,
        'bedroom_choices' : bedroom_choices,
        'state_choices' : state_choices,
        'listings' : queryset_list,
        'values' : request.GET
    }
    return render(request, "listings/search.html", context ) 