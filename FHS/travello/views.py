from django.shortcuts import render
from . models import Destination,Hotels,Room,Section,Option,Item,Address

def foodHome(request):
        sections=Section.objects.all()
        
        un=request.user.username
        print(un)
        if(un=='saisadanandhk'):
                        r1=Item.objects.all().filter(link='s1')
        if(un=='sainadh'):
                        r1=Item.objects.all().filter(link='s2')
        if(un=='nithin'):
                        r1=Item.objects.all().filter(link='s3')
        if(un=='prasanna'):
                        r1=Item.objects.all().filter(link='s4')
        '''test=Item.objects.all().filter(link='s1')
        t=[r1,test]   
        print(r1)
        print(t)
        for i in t:
                for x in i:
                        print(x.name)'''
        return render(request,'foodHome.html',{'sections':sections,'sg':r1})

def veg(request):
        
        type='veg'
        options=Option.objects.all().filter(type=type)
        return render(request,'options.html',{'options':options})
def nonveg(request):
        type='nonveg'
        options=Option.objects.all().filter(type=type)
        return render(request,'options.html',{'options':options})
def desserts(request):
        type='desserts'
        options=Option.objects.all().filter(type=type)
        return render(request,'options.html',{'options':options})
def vegBiriyanis(request):
        link='biriyani'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def vegStarters(request):
        link='starters'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def vegCurries(request):
        link='curries'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def Rotis(request):
        link='rotis'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def nonVegBiriyanis(request):
        link='nbiriyani'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def nonVegStarters(request):
        link='nstarters'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def nonVegCurries(request):
        link='ncurries'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def icecreams(request):
        link='icecreams'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def drinks(request):
        link='drinks'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def cakes(request):
        link='cakes'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def sweets(request):
        link='sweets'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def milkshakes(request):
        link='milkshakes'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})
def cookies(request):
        link='cookies'
        items=Item.objects.all().filter(link=link)
        return render(request,'items.html',{'items':items})

def fsearch(request):
        s=request.GET['input1']
        print(s)
        if Item.objects.all().filter(name=s).exists:
                t=Item.objects.all().filter(name=s)
        elif Option.objects.all().filter(name=s).exists:
                t=Option.objects.all().filter(name=s)
        print(t)
        x=Item.objects.all().filter(id=6)
        print(x)
        for i in x:
                print(i.name)
        return render(request,'fsearch.html',{'item':t})

def book(request):
        addr1=Address()
        addr1.name=request.POST['name']
        addr1.number=request.POST['number']
        addr1.pincode=request.POST['pincode']
        addr1.area=request.POST['area']
        addr1.city=request.POST['city']
        addr1.state=request.POST['state']

        confirm='your order has been placed successfuly...!'
        
        return render(request,'success1.html',{'confirm':confirm,'home':'foodHome','img':'fh2','address':addr1})
def address(request):
        return render(request,'address.html')


def success2(request):
        confirm='you order has been placed successfuly...!'
        return render(request,'success1.html',{'confirm':confirm,'home':'foodHome','img':'fh2'})

















# Create your views here.
def search1(request):
        name=request.GET['input1']
        print(name)
        tests=Destination.objects.all().filter(name=name)
        return render(request,'search.html',{'tests':tests,'link':'destinations'})
def search2(request):
        name=request.GET['input1']
        print(name)
        tests=Hotels.objects.all().filter(name=name)
        return render(request,'search.html',{'tests':tests,'link':'rooms'})
def search3(request):
        name=request.GET['input1']
        print(name)
        tests=Room.objects.all().filter(name=name)
        return render(request,'search.html',{'tests':tests,'link':'rooms'})
        

        
        
    

def rooms(request):
    rooms=Room.objects.all()

    return render(request,'rooms.html',{'rooms':rooms})

def dest(request):
    hotels=Hotels.objects.all()

    return render(request,'destinations.html',{'Hotels':hotels})
def index(request):
    '''#obj1
    dest1=Destination()
    dest1.name='Mumbai'
    dest1.description='this is a place of street foods'
    dest1.img='destination_1.jpg'
    dest1.price=400
    dest1.offer=False'''
    
    dests=Destination.objects.all()
    
    return render(request,'index.html',{'dests':dests})


def success1(request):
        confirm='you Room has been booked successfuly...!'
        return render(request,'success1.html',{'confirm':confirm,'home':'/','img':'hotel_home'})

def aboutUs(request):
        return render(request,'aboutUs.html')
