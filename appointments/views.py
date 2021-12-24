from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def home(request):

    name = "Home"
    context = {
        'name':name
    }
    return render(request , 'appointments/home.html',context)

def about(request):

    name = "About"
    context = {
        'name':name
    }
    return render(request , 'appointments/about.html',context)

def gallery(request):

    name = "Gallery"
    context = {
        'name':name
    }
    return render(request , 'appointments/Gallery.html',context)    

def contact(request):

    name1 = "Contact"

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message
        }

        message = '''
        name: {}
        New Message : {}

        From : {}
        '''.format(data['name'],data['message'],data['email'])

        send_mail(data['subject'],message,'',['monyemangene.2@gmail.com'])

    context = {
        'name':name1
    }
    return render(request , 'appointments/contact.html',context)