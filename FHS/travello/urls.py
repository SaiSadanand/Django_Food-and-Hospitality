from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('aboutUs',views.aboutUs,name='aboutUs'),
    path('destinations',views.dest,name='destinations'),
    path('rooms',views.rooms,name='rooms'),
    path('search1',views.search1,name='search1'),
    path('search2',views.search2,name='search2'),
    path('search3',views.search3,name='search3'),
    path('foodHome',views.foodHome,name='foodHome'),
    path('fsearch',views.fsearch,name='Result'),
    path('veg',views.veg,name='veg'),
    path('nonveg',views.nonveg,name='nonveg'),
    path('desserts',views.desserts,name='desserts'),
    path('biriyani',views.vegBiriyanis,name='vegBiriyanis'),
    path('starters',views.vegStarters,name='vegStarters'),
    path('curries',views.vegCurries,name='vegCurries'),
    path('nbiriyani',views.nonVegBiriyanis,name='nonVegBiriyanis'),
    path('nstarters',views.nonVegStarters,name='nonVegStarters'),
    path('ncurries',views.nonVegCurries,name='nonVegCurries'),
    path('rotis',views.Rotis,name='Rotis'),
    path('icecreams',views.icecreams,name='IceCreams'),
    path('drinks',views.drinks,name='SoftDrinks'),
    path('cakes',views.cakes,name='Cakes'),
    path('cookies',views.cookies,name='Cookies'),
    path('sweets',views.sweets,name='Sweets'),
    path('milkshakes',views.milkshakes,name='MilkShakes'),
    path('success1',views.success1,name='RoomConfirmed'),
    path('success2',views.success2,name='OrderConfirmed'),
    path('book',views.book,name='orderConfirmation'),
    path('address',views.address,name='AddressPage')
]