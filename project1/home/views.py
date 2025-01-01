from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'about/about.html')

def contact(request):
    if request.method == "POST":
        
        email = request.POST.get('email')
        password = request.POST.get('message')
        
        Contact.objects.create( email=email, password=password)
        messages.success(request, "Thank you! Your message has been sent successfully.")
        # Contact.save()
    return render(request, 'contact/contact.html')

def service(request):
    return render(request, 'service/service.html')


