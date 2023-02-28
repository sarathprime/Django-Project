from django.shortcuts import render, redirect
from .models import *
# from administrator.models import *
from django.http import HttpResponse
from django.contrib import messages
from fabrication.models import *




def c_index(request):
    return render(request,'consumer/consumer_index.html')

def c_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        consumer(username=username, email=email, password=password, phonenumber=phonenumber,
                 address=address).save()
        messages.info(request, "successfully registered")
        return redirect('/c_login/')
    return render(request, 'consumer/c_login.html')

def c_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            emp = fabrication.objects.get(email=email, password=password)
            request.session['consumer'] = emp.email

            messages.info(request, "successfully login")

            return redirect('/c_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'consumer/c_login.html')


def c_details(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        country = request.POST['country']
        message = request.POST['message']
        company_Details(company_name=company_name, email=email, pincode=pincode, country=country,
                 message=message,state=state,city=city).save()
        messages.info(request, "Details updated successfully")
        return redirect('/c_requirement/')
    return render(request,'consumer/c_details.html')


def c_requirement(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        email = request.POST['email']
        type = request.POST['type']
        product = request.POST['product']
        product1 = request.POST['product1']
        product2 = request.POST['product2']
        quantatiy = request.POST['quantatiy']
        queries = request.POST['queries']
        requirement(company_name=company_name, email=email, type=type, product=product,
                        product1=product1, product2=product2, quantatiy=quantatiy,queries=queries).save()
        messages.info(request, "requirement updated sucessfully")
        return redirect('/c_index/')
    data = company_Details.objects.all()

    return render(request,'consumer/requirement.html',{'data':data})



def C_logout(request):
    if 'consumer' in request.session:
        request.session.pop('consumer',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/F_logout/')


def DELIVERED(request):
    datas = requirement.objects.all()
    return render(request, 'consumer/delievered_p.html', {'datas': datas})