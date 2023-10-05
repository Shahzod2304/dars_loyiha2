from django.shortcuts import render
from .models import * 
# Create your views here.
def Home(request):
    caffee = Cafe_Name.objects.all()
    menu = Menu.objects.all()
    about = About_Cafe.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact_us(name=name, email=email, message = message)
        contact.save()

    context = {
        'caffee':caffee,
        'menu':menu,
        'about':about
    } 
    return render(request, 'index.html', context)




