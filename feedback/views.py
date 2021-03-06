from django.shortcuts import render, HttpResponse, redirect
from .models import Feedback
from users.models import Outlet
from .serializers import FeedbackSerializer
from datetime import datetime
from django.contrib import messages
from rest_framework.renderers import JSONRenderer
from django.views.generic import View,DetailView
from feedback.forms import ContactForm
import re
# Create your views here.


def is_email_vaild(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return True

    else:
        False

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'outlets': Outlet.objects.filter(verified=True)
        }
        return render(request, 'home/index.html', context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/about.html')

def contactus(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if (is_email_vaild(email)):
            name = request.POST.get('name')
            message = request.POST.get('message')
            date = datetime.today()
            contact = Feedback(name=name, email=email, message=message, date=date)
            contact.save()
            messages.success(request, 'Thank you for reaching out to us!!')
            return render(request, 'home/index.html')
        else:
            messages.error(
                request, f'Invalid Email')
            return render(request, 'home/contactus.html')
    return render(request, 'home/contactus.html')

# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'home/contactus.html')

#     def post(self, request, *args, **kwargs):
#         form = ContactForm(request.POST)
#         email = request.POST.get('Email')
#         print(email)
#         if form.is_valid():
#             p = form.save()
#             messages.success(request, 'Thank you for reaching out to us!!')
#             return redirect('home')
#         return render(request, 'home/contactus.html')


class OutletView(View):
    def get(self, request,pk, *args, **kwargs):
        context = {
            'outlet': Outlet.objects.get(id=pk)
        }
        return render(request, 'home/outlet.html', context)



# def outlet(request, pk):
#     context = {
#         'outlet': Outlet.objects.get(id=pk)
#     }
#     return render(request, 'home/outlet.html', context)




# def index(request):
#     context = {
#         'outlets': Outlet.objects.filter(verified=True)
#     }
#     return render(request, 'home/index.html', context)


# def login(request):
#     return render(request, 'Login/login.html')


# def signup(request):
#     return render(request, 'Login/signup.html')


# def detail(request, pk):
#     det = Contact.objects.get(id=pk)
#     serializer = ContactSerializer(det)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data)


# def detail_all(request):
#     det = Contact.objects.all()
#     serializer = ContactSerializer(det, many=True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data)


# def about(request):
#     return render(request, 'home/about.html')
