from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    
    people = [
        {'name': 'sayan', 'age': 23},
        {'name': 'Sankho', 'age': 20},
        {'name': 'Raju', 'age': 16},
        {'name': 'Shreyas', 'age': 17}
    ]
    
    text = """
    Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.[28][29][30] Their long occupation, predominantly in isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity.[31] Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of the third millennium BCE.[32] By 1200 BCE, an archaic form of Sanskrit, an Indo-European language, had diffused into India from the northwest.[33][34] Its hymns recorded the dawning of Hinduism in India.[35] India's pre-existing Dravidian languages were supplanted in the northern regions.[36] By 400 BCE, caste had emerged within Hinduism,[37] and Buddhism and Jainism had arisen, proclaiming social orders unlinked to heredity.
    """
    
    
    
    return render(request, 'index.html', context = {'people' : people, 'text' : text})

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def ecomerce(request):       
    return render(request, 'ecomerce/index.html', context = {'page' : 'Everythinng Delivered in a minuts | Blinkit'})

def product(request):
    return render(request, 'ecomerce/product.html')

def contactus(request):
    return render(request, 'ecomerce/contact.html', context = {'page' : 'Contact us'})

def aboutus(request):    
    return render(request, 'ecomerce/about.html', context = {'page' : 'About us'})

    
def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

# def home(request):
#     return HttpResponse("<h1>Hello, World!</h1>")
