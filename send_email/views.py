from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject') 
        message = request.POST.get('message')
        context = {
            'name': name,
            'email': email,
            'phone':phone,
            'subject': subject,
            'message': message
        }
        message = '''
        New message: {}
        Email: {}
        Phone number: {}
        '''.format(context['message'], context['email'], context['phone'])
        send_mail(context['subject'], message, '', ['baratovmuzrob@gmail.com'])
        return HttpResponse("Xabaringiz jo'natildi... Tez orada siz bilan bog'lanamiz!")
    return render(request, 'index.html', {})