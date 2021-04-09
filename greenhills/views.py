from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta, date
import sqlite3
import json
import os
from .expiry import *
from .models import UserPayments


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        userName = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['psw']
        password2 = request.POST['psw2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "user already registerd")
            else:
                user = User.objects.create_user(username=userName, email=email, password=password1)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, "Passwords not matching")

    return render(request, 'register.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        userName = request.POST['email']
        password = request.POST['psw']

        user = auth.authenticate(username=userName, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid username or password")

    return render(request, 'login.html')


def plans(request):
    product_name = request.GET.get('products', None)
    flag_name = request.GET.get('flag', None)
    email_name = request.GET.get('email', None)
    paid_date = request.GET.get('paid_date', None)

    print(product_name)

    if request.method == 'POST':
        product_name = request.GET.get('products', None)
        con = sqlite3.connect('db.sqlite3')
        cursor = con.cursor()
        tableCmd = "SELECT * FROM products where product_name =" + product_name
        print(tableCmd)
        res = cursor.execute(tableCmd)

    return render(request, 'buyplan.html',
                  {"product_name": product_name, "flag": flag_name, "email": email_name, "paid_date": paid_date})


def payments(request):
    month = request.GET.get('month', None)
    product_name = request.GET.get('product_name', None)
    flag_name = request.GET.get('flag', None)
    email_name = request.GET.get('email', None)
    paid_date = request.GET.get('paid_date', None)
    if request.method == 'POST':
        email = request.POST['email']
        month = request.POST['month']
        month = int(month)
        product_name = request.POST['product-name']

        try:
            paid_date = request.POST['paid-date']
            flag = request.POST['flag']
        except:
            paid_date = 0
            flag = 0

        if flag:
            payment = UserPayments.objects.filter(email=email, product_name=product_name)
            for i in payment:
                i.expiry_date = i.expiry_date + timedelta(days=month * 30)
                i.save()
                return redirect('/')
        else:
            product_name = request.POST['product-name']
            payment = UserPayments()
            payment.email = email
            payment.product_name = product_name
            payment.paid_date = datetime.now()
            payment.expiry_date = datetime.now() + timedelta(month * 30)
            payment.price_paid = 99 * month
            payment.subscription = month
            payment.save()
            return redirect('/')

    return render(request, 'payments.html', {'month': month, 'product_name': product_name, "flag": flag_name,
                                             "email": email_name, "paid_date": paid_date})


@csrf_exempt
def userplans(request):
    email = request.GET.get('email', None)
    products = UserPayments.objects.filter(email=email)
    if request.method == 'POST':
        data = request.POST.getlist('data[]')
        email = data[0]
        product_name = data[1]
        pause_month = int(data[2])
        print(data)
        payment = UserPayments.objects.filter(email=email, product_name=product_name)
        for user in payment:
            paid_date = user.expiry_date - date.today()
            diff_days = int(paid_date.days)
            expiry_date = date.today() + timedelta(days=(pause_month * 30) + diff_days)
            user.expiry_date = expiry_date
            paid_date = date.today() + timedelta(days=pause_month * 30)
            user.paid_date = paid_date
            user.save()
        # payment.expiry_date = datetime.now() + timedelta(month * 30)

    return render(request, 'plans.html', {'products': products})


def expirycheck(request):
    expired_check()
    return render(request,'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
