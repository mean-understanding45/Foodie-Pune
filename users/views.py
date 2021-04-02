from .models import Outlet
from .serializers import OutletSerializer
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import View, DetailView
from users.forms import OutletForm
import re
# Create your views here.


def is_email_vaild(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return True

    else:
        False


class OutletView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login/register_outlet.html')


@login_required
def registerOutlet(request):
    if request.method == "POST" and request.FILES['outlet_img']:
        email = request.POST.get('Email')
        if (is_email_vaild(email)):
            outlet_img = request.FILES['outlet_img']
            fs = FileSystemStorage()
            filename = fs.save(outlet_img.name, outlet_img)
            uploaded_file_url = fs.url(filename)
            user = request.user.username
            outletname = request.POST.get('OutletName')
            foodtype = request.POST.get('FoodType')
            homedelivery = request.POST.get('HomeDelivery')
            ownerfirstname = request.POST.get('OwnerFirstName')
            ownerlastname = request.POST.get('OwnerLastName')
            address = request.POST.get('Address')
            addresslink = request.POST.get('AddressLink')
            phone = request.POST.get('Phone')

            outlet = Outlet(outletname=outletname, foodtype=foodtype, homedelivery=homedelivery, ownerfirstname=ownerfirstname, ownerlastname=ownerlastname,
                            address=address, image=filename, addresslink=addresslink, email=email, phone=phone)
            outlet.save()
            messages.success(
                request, f'Thank You!! Our team will get to you soon!! ')
            return redirect('home')
        else:
            messages.error(
                request, f'Invalid Email')
            return render(request, 'login/register_outlet.html')
    return render(request, 'login/register_outlet.html')


def signupUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if (is_email_vaild(email)):
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            if password == repassword:
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                try:
                    user = User.objects.get(username=email)
                    messages.error(
                        request, f'User already exits ')
                    return render(request, 'login/signup.html')
                except User.DoesNotExist:
                    user = User.objects.create_user(
                        username=email, email=email, password=password)
                    user.is_active = True
                    user.first_name = firstname
                    user.last_name = lastname
                    user.save()
                    messages.success(
                        request, f'Your account created successfully!!')
                    login(request, user)
                    return redirect('home')
            else:
                messages.error(
                    request, f'Passwords you provided dont match')
                return render(request, 'login/signup.html')
    return render(request, 'login/signup.html')


def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are successfully logged in!!')
            return redirect('home')
        else:
            messages.error(request, f'Username OR password is incorrect')
    return render(request, 'login/login.html')


@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, 'You are successfully logged out!!')
    return redirect('login')


def forgot(request):
    return render(request, 'login/forgot.html')

# class OutletCreate(CreateView):
#     model = User
#     fields = '__all__'
#     success_url = reverse_lazy('home')

#     # def get(self, request, *args, **kwargs):
#     #     return render(request, 'login/register_outlet.html')

#     # def post(self, request, *args, **kwargs):
#     #     form = OutletForm(request.POST)
#     #     if form.is_valid():
#     #         p = form.save()
#     #         messages.success(
#     #             request, f'Thank You!! Our team will get to you soon!! ')
#     #         return redirect('home')
#     #     messages.success(request, f'wrong ')
#     #     return render(request, 'login/register_outlet.html')


# class SignupUserView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'login/register_outlet.html')

#     def post(self, request, *args, **kwargs):
#         form = OutletForm(request.POST)
#         if form.is_valid():
#             p = form.save
#             messages.success(
#                 request, f'Thank You!! Our team will get to you soon!! ')
#             return redirect('home')
#         return render(request, 'login/register_outlet.html')


# class LoginUserView(View):
#     def get(self,request,*args,**kwargs):
#         return render(request, 'login/login.html')

#     def post(self,request,*args,**kwargs):
