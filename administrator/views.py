from django.shortcuts import render, redirect
from .models import *
# from administrator.models import *
from django.http import HttpResponse
from django.contrib import messages
from fabrication.models import *
from consumer.models import *
from dealer.models import *
from django.core.mail import send_mail
import numpy as np
import pandas as pd
import warnings
from django.contrib import admin,messages
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import ExtraTreesClassifier




def a_index(request):
    return render(request,'admin/ai_index.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == "admin@gmail.com" and password == "admin":
            request.session['admin'] = 'admin@gmail.com'
            messages.info(request, "successfully login")
            return redirect('/a_index/')
        elif username != "admin@gmail.com":
            messages.error(request, "Wrong Admin Email")
            return redirect('/admin_login/')
        elif password != "admin":
            messages.error(request, "Wrong Admin Password")
            return render(request, 'admin/admin_index.html')
    return render(request, 'admin/a_login.html')



def view_stock(request):
    datas = current_stock.objects.filter(stockss=False)
    return render(request,'admin/view_stock.html',{'datas': datas})

def C_stock(request,id):
    datas = current_stock.objects.get(id=id)
    datas.stockss = True
    datas.save()
    messages.success(request, 'Aspect successfully')
    return redirect('/a_index/')

def view_client(request):
    datas = company_Details.objects.all()
    return render(request,'admin/view_client.html',{'datas': datas})

def algo(datas,r):
    data = pd.read_csv('project 5.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = ExtraTreesClassifier()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]



def get_input(request, id):
    # if 'user' in request.session:
    get = requirement.objects.get(id=id)
    r=get.id
    get.approves = True
    get.save()
    inputvar = []
    get.save()

    type = get.type
    product= get.product
    product1= get.product1
    product2= get.product2
    quantatiy = get.quantatiy

    inputvar.append(type)
    inputvar.append(product)
    inputvar.append(product1)
    inputvar.append(product2)
    inputvar.append(quantatiy)

    print('input:', inputvar)
    ka = algo(inputvar,r)
    print('OUTPUT:',ka)
    # messages.info(request, "Completed analysyis")
    st = requirement.objects.filter(id=r).update(materails=ka)
    return redirect('/find_raw/')


def Request(request):
    datas = requirement.objects.all()
    return render(request,'admin/product_request.html',{'datas': datas})



def find_raw(request):
    datas = requirement.objects.filter(b2=False)
    return render(request,'admin/find_rawmaterails.html',{'datas': datas})

def C_fr(request,id):
    datas = requirement.objects.get(id=id)
    datas.b2 = True
    datas.save()
    messages.success(request, 'Sucessfully send to molding team')
    return redirect('/a_index/')




def loading(request):
    messages.success(request, 'Aspect successfully')
    return render(request,'admin/loading.html')

def send_m(request):
    if request.method == 'POST':
        product = request.POST['product']
        range = request.POST['range']
        query = request.POST['query']
        send_mold(product=product, range=range, query=query,
                 ).save()
        messages.info(request, "materials updated to molding team")
        return redirect('/a_index/')
    return render(request, 'admin/send_m.html')




def view_payment(request):
    datas = pay_slip.objects.all()
    return render(request,'admin/view_payment.html',{'datas': datas})


def credit_card(request):
    return render(request,'admin/pay.html')



def final_payment(request):
    # datas = dealer.objects.all()
    # print(datas.email)
    # print(datas.refer)
    # send_mail(
    #     'Subject here',
    #     'Congrats! ,  PAYMENT SUCESSFULL ',
    #     'sarathkumarjsurya@gmail.com',
    #     [datas.email],
    #     fail_silently=False,
    # )
    # datas.approve = True
    #
    # datas.save()
    print('1')

    return redirect('/a_index/')

def A_logout(request):
    if 'admin' in request.session:
        request.session.pop('admin',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/admin/')