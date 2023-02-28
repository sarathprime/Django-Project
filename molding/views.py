from django.shortcuts import render,redirect
from .models import *
# from administrator.models import *
from django.http import HttpResponse
from django.contrib import messages
from fabrication.models import *
from consumer.models import *
from administrator.models import *
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import HistGradientBoostingClassifier

def molding_index(request):
    return render(request,'molding/molding_index.html')

def m_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        molding(username=username, email=email, password=password, phonenumber=phonenumber,
                 address=address).save()
        messages.info(request, "successfully registered")
        return redirect('/m_login/')
    return render(request, 'molding/m_login.html')

def m_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            emp = molding.objects.get(email=email, password=password)
            request.session['molding'] = emp.email

            messages.info(request, "successfully login")

            return redirect('/molding_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'molding/m_login.html')


def view_Admin(request):
    datas = send_mold.objects.filter(silicon_r=False)
    return render(request,'molding/view_admin.html',{'datas': datas})





def algo(datas,r):
    data = pd.read_csv('5.23.csv')
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

    model = HistGradientBoostingClassifier()
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



def get_inputs(request, id):
    # if 'user' in request.session:
    get = send_mold.objects.get(id=id)
    r=get.id
    get.approves = True
    get.save()
    inputvar = []
    get.save()

    product = get.product
    range= get.range
    query= get.query


    inputvar.append(product)
    inputvar.append(range)
    inputvar.append(query)

    print('input:', inputvar)
    ka = algo(inputvar,r)
    print('OUTPUT:',ka)
    messages.info(request, "Completed analysyis")
    st = send_mold.objects.filter(id=r).update(solutionss=ka)
    return redirect('/analysing/')


def m_need(request):
    datas = send_mold.objects.all()
    return render(request,'molding/material_needed.html',{'datas': datas})



def analysing(request):
    return render(request,'molding/analysing.html')

def view_table(request):
    if request.method == 'POST':
        computer = request.POST['computer']
        electronics = request.POST['electronics']
        ceramics = request.POST['ceramics']
        purchase(computer=computer, electronics=electronics, ceramics=ceramics
                ).save()
        messages.info(request, "Cart updated to distributor")
        return redirect('/molding_index/')
    return render(request,'molding/table.html')





def Teaam_register(request):
    if request.method == 'POST':
        Team = request.POST['Team']
        Email = request.POST['Email']
        team_register(Team=Team, Email=Email,
                 ).save()
        return redirect('/view_table/')
    return render(request,'molding/team_register.html')


def view_dropped(request):
    datas = purchase.objects.filter(s=True)
    return render(request, 'molding/dropped.html', {'datas': datas})


def molding_process(request):
    return render(request,'molding/process.html')

def molded_products(request):
    if request.method == 'POST':
        silicon = request.POST['silicon']
        quantatiy = request.POST['quantatiy']
        product_send(silicon=silicon,quantatiy=quantatiy
                     ).save()
        messages.info(request, "Molded products sucessfully sended to fabrication")
        return redirect('/molding_index/')
    return render(request,'molding/molded_products.html')


def M_logout(request):
    if 'molding' in request.session:
        request.session.pop('molding',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/F_logout/')

