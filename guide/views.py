from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import register
from.models import login
from.models import booking
from.models import buss
from django.contrib import messages

def display(request):
    return render(request,'index.html')
def add(request):
    if request.method=="POST":
        a=request.POST['n1']
        b=request.POST['n2']
        c=int(request.POST['n3'])
        d=int(request.POST['n4'])
        e=int(request.POST['n5'])
        data=register.objects.create(username=a,password=b)
        data.save()
        data1=login.objects.create(USERNAME=a, PASSWORD=d,status=1)
        data1.save()

        r=login.objects.get(USERNAME=a)
        request.session['id']=a 
        return render(request,'login.html')

        return redirect('login')
def profile(request):
    if 'id' in request.session:#session check
        return render(request,'index.html')
    else:
        return redirect(login)

def log(request):
    if request.method=="POST":
        a=request.POST['n1']#username
        d=int(request.POST['n4'])#password
        try:
            r=login.objects.get(USERNAME=a)
            if r.PASSWORD==d and r.status==1:
                request.session['id']=a #session created
                return render(request,'login.html')
            elif r.PASSWORD==d and r.status==0:
                request.session['id']=a  #session created
                return render(request,'admn.html')
            else:
                return HttpResponse("password incorrect")
        except Exception:
            return HttpResponse("username incorrect")
    else:
        return render(request,'index.html')
def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return render(request,'index.html')
def service(request):
    return render(request,'services.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def destination(request):
    return render(request,'destin.html')
def himalayan(request):
    return render(request,'himalaya.html')
def resort(request):
    return render(request,'hresort.html')
def book(request):
    if request.method=="POST":
        w = request.POST['s1']
        x = request.POST['s2']
        y = int(request.POST['s3'])
        z = request.POST['s4']
        v = int(request.POST['s5'])#people
        u = int(request.POST['s6'])
        # o = request.POST['s7']#checkin
        # p = request.POST['s8']#checkout
        # h=p-o
        # print(h)
        j=v*1500
        data = booking.objects.create(NAME=w, EMAIL=x, PHONENUMBER=y, PLACE=z, PEOPLE=v, PROOF=u , AMOUNT=j)
        data.save()
        data1=booking.objects.filter(NAME=w)

        # messages.info(request,'successfully booked!!')
        return render(request,'bill.html',{'b':data})
def go(request):
    return render(request,'goa.html')
def aagran(request):
    return render(request,'aagra.html')
def maha(request):
    return render(request,'maharashtra.html')
def oot(request):
    return render(request,'ooty.html')
def hydh(request):
    return render(request,'hyderabad.html')
def aass(request):
    return render(request,'aassam.html')
def bangalu(request):
    return render(request,'bangaloor.html')
def resogoa(request):
    return render(request,'gresort.html')
def resoagra(request):
    return render(request,'agresort.html')
def resomaha(request):
    return render(request,'maresort.html')
def resoot(request):
    return render(request,'ooresort.html')
def resohy(request):
    return render(request,'hyresort.html')
def resoass(request):
    return render(request,'aasresort.html')
def resoban(request):
    return render(request,'baresort.html')
def room(request):
    return render(request,'rooms.html')
def bus(request):
    return render(request,'bbus.html')
def bbook(request):
    if request.method=="POST":
        p = request.POST['a1']
        q = int(request.POST['a2'])
        r = request.POST.get('a3', '')
        s = request.POST['a4']
        t = int(request.POST['a5'])
        # data2 = buss.objects.create(NAME=p, PHONENUMBER=q, TO=r, FROM=s, PEOPLE=t)
        # data2.save()
        if r=="himalaya":
            v=t*3500
            data2 = buss.objects.create(NAME=p,PHONENUMBER=q,FROM=s,PEOPLE=t,AMOUNT=v, TO=r)
            data2.save()
            data3 = buss.objects.filter(NAME=p)
            return render(request, 'bill3.html', {'a': data2})
        elif r=="goa":
            v=t*1000
            data2 = buss.objects.create(NAME=p,PHONENUMBER=q,FROM=s,PEOPLE=t,AMOUNT=v, TO=r)
            data2.save()
            data3 = buss.objects.filter(NAME=p)
            return render(request, 'bill3.html', {'a': data2})
        elif r=="aagra":
            v=t*2000
            data2 = buss.objects.create(NAME=p,PHONENUMBER=q,FROM=s,PEOPLE=t,AMOUNT=v, TO=r)
            data2.save()
            data3 = buss.objects.filter(NAME=p)
            return render(request, 'bill3.html', {'a': data2})
        elif r=="maharashta":
            v=t*1500
            data2 = buss.objects.create(NAME=p,PHONENUMBER=q,FROM=s,PEOPLE=t,AMOUNT=v, TO=r)
            data2.save()
            data3 = buss.objects.filter(NAME=p)
            return render(request, 'bill3.html', {'a': data2})
        elif r=="ooty":
            v=t*2000
            data2 = buss.objects.create(NAME=p,PHONENUMBER=q,FROM=s,PEOPLE=t,AMOUNT=v, TO=r)
            data2.save()
            data3 = buss.objects.filter(NAME=p)
            return render(request, 'bill3.html', {'a': data2})
        elif r=="hyderabad":
            v=t*2500
            data2 = buss.objects.create(NAME=p,PHONENUMBER=q,FROM=s,PEOPLE=t,AMOUNT=v, TO=r)
            data2.save()
            data3 = buss.objects.filter(NAME=p)
            return render(request, 'bill3.html', {'a': data2})
        elif r=="aasam":
            v=t*2000
            data2 = buss.objects.create(NAME=p,PHONENUMBER=q,FROM=s,PEOPLE=t,AMOUNT=v, TO=r)
            data2.save()
            data3 = buss.objects.filter(NAME=p)
            return render(request, 'bill3.html', {'a': data2})
        else:
            v=t*1000
            data2 = buss.objects.create(NAME=p,PHONENUMBER=q,FROM=s,PEOPLE=t,AMOUNT=v, TO=r)
            data2.save()
            data3 = buss.objects.filter(NAME=p)
            return render(request, 'bill3.html', {'a': data2})
        # messages.info(request,'booked!!')
        # return render(request,'bbus.html')


def card_payment(request, amount):
    # if request.method == "POST":
    #     return render(request, 'payment_success.html')
    return render(request, 'payment.html',{'amount':amount})

def process_payment(request):
    return render(request, 'payment_success.html')

def book_room(request, room_type):
    room_rate = {
        'double':[1000,'Double Room'], 
        'deluxe':[1500,'Deluxe Double Room'],  
        'twin':[2000,'Twin Room'], 
        'single_twin':[1400,'Single Twin Room'], 
        'triple':[1700,'Triple Room'], 
        'single':[700,'Single Room']}
    
    room = room_rate[room_type]
    room_name = room_rate[room_type][1]
    print(room)
    return render(request, 'book_room.html', {'room_name':room_name, 'room_type': room_type})

def r_booking(request, room_type):
    room_rate = {
        'double':[1000,'Double Room'], 
        'deluxe':[1500,'Deluxe Double Room'],  
        'twin':[2000,'Twin Room'], 
        'single_twin':[1400,'Single Twin Room'], 
        'triple':[1700,'Triple Room'], 
        'single':[700,'Single Room']}
    price = room_rate[room_type][0]
    
    room_name = room_rate[room_type][1]
    if request.method=="POST":
        name = request.POST['name']
        ph_number = int(request.POST['ph_number'])
        email = request.POST['email']
        n_days = request.POST['n_days']
        total = price*int(n_days)
        return render(request, 'room_bill.html', {
            'name':name, 'ph_number':ph_number, 
            'total':total, 'room_name':room_name,
            'email':email, 'n_days':n_days
            })


#Create your views here.
