import random
import uuid
from asyncio import format_helpers

from django import forms
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from paypal.standard.forms import PayPalPaymentsForm

from .models import *



   

def login_registrar(request):

    if request.method == 'POST':
        user = User()
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            error_message = "Las contraseñas no coinciden"
            print(error_message)
            return render(request,'registration/login_registrar.html', {'error': error_message})
        print('Las contraseñas coinciden')

        email = request.POST['email']
        first_name = request.POST['first_name']

        if User.objects.filter(username=username).exists():
            user_exists_error_message = "Este usuario ya existe"    
            return render(request,'registration/login_registrar.html', {'error': 'Usuario o contraseña incorrectos'})
        
        else:
            user.username = username
            user.email = email
            user.first_name = first_name
            user.set_password(password)
            user.save()
            return redirect('/inicio/')
        
    return render(request, 'registration/login_registrar.html')




def index(request):
    wellcomestart = WellcomeStart.objects.all()
    box_tours = Box_tours.objects.all()
    randon_tours = Box_tours.objects.all()

    randon_tours = random.randint(0, randon_tours.count())

    filter_tours_random = Box_tours.objects.all()
    for tou in filter_tours_random:
            print(tou.name_tour,'Aquisition') 
    
    return render(request, 'app/index.html',
    {
        'wellcomestart': wellcomestart,
        'box_tours': box_tours,
        'filter_tours_random': filter_tours_random  })



@login_required
def inicio(request):
    return render(request, 'app/inicio.html')


def login(request):
    logout(request)
    return redirect('/')



@login_required
def get_tours(request, paquete):
    box_tours = Box_tours.objects.filter(id=paquete)
    for box in box_tours:
        print(box.name_tour)
    user_get_paquet = User.objects.get(id=request.user.id)
    tours = Box_tours.objects.filter(id=paquete) 
    save = User.objects.get(id=request.user.id)

    PAYPAL_RECEIVER_EMAIL  = 'sb-easix25999816@business.example.com'
g    price =12

    paypal_dict = {
        "business": PAYPAL_RECEIVER_EMAIL,
        "amount": price ,
        "item_name": "El sol del la mirada",
        "invoice": str(uuid.uuid4()),
        "currency_code": "USD",
        "notify_url": "" ,
        "return": '' ,
        "cancel_return": "",
        # "": PAYPAL_BUY_BUTTON_IMAGE,
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    

        
    
    print('no for')
    if request.method == 'POST':
        print('if post request')
        asientos = request.POST.get("asientos")
        if asientos is not None:
                listo = int(asientos)
                number_asientos = int

                delete_a_asientos = Box_tours.objects.filter(id=paquete)
                for asientos in delete_a_asientos:
                    number_asientos =  asientos.asientos
                    price = asientos.price
                    print(number_asientos)

                if number_asientos <= 0:
                    for asientos in delete_a_asientos:
                        asientos.asientos = 0
                        asientos.save()
                else:
                    for asientos in delete_a_asientos:
                     asientos.asientos = number_asientos - listo
                    asientos.save()
                        # else:
                        #      print('es igual a 0')


                get_buy_tours =  Box_tours.objects.filter(id=paquete) 
                for buy in get_buy_tours:
                        buys = buy.get_buy_tours_set.create(number_get_buy=1)
                        # print(buys)

                for tour in tours:
                        get_paquet = save.tour_user_model_set.create(name=tour.name_tour, number_id_tour=paquete)
                        messeje_get_buy = 'Adquerido su Tour', tour.name_tour
                        print(messeje_get_buy)
                        
    return render(request, 'app/get_tours.html',  
                  {'box_tours': box_tours,
                   "form": form})




def blog(request):
    post = Blog.objects.all()

    return render(request, 'app/blog.html', {'post': post})




def faq(request):
    faq = Faq.objects.all()
    return render(request, 'app/faq.html', {'faq': faq})




@login_required
def tours(request): 
    if request.user.is_authenticated:
        print(request.user.id)
    else:
        print('No hay nadie autenticaco en este momento')

    box_tours = Box_tours.objects.all()
    return render(request, 'app/tours.html', {'box_tours': box_tours})




@login_required
def perfil(request):

    if request.user.is_authenticated:
        # user_registrado verifica que el usuario esta logueado
        user_registrado = User.objects.get(pk=request.user.id)
        # user hace se usa para identificar el usuario para buscar la llave foranea
        user = User.objects.filter(pk=request.user.id)
        # tours_getting obtiene el historial de tours de ese usuario
        tours_getting = user_registrado.tour_user_model_set.all()

        print(request.user.id, user_registrado)

        # from django.core.mail import send_mail

        # send_mail(
        #     "Subject here",
        #     "Here is the message.",
        #     "wandy.oli@icloud.com",
        #     ["wandy.oli@icloud.com"],
        #     fail_silently=False,)
        

    else:
        print('No hay nadie autenticado en este momento')

    return render(request, 'app/perfil.html', 
                  {'user': user,
                   'tours_getting':tours_getting},)




# Admin Site Views

@login_required
def admin_site(request):
    return render(request, 'app/admin_site/admin_site.html')


# Esta vista cra los BOX_Tours 
def paque_tour(request):

    box_tours = Box_tours.objects.all()

    if request.method == 'POST':
   
        box_toura_add = Box_tours()
        box_toura_add.name_tour  = request.POST.get("name")
        print(box_toura_add.name_tour)
        box_toura_add.asientos = request.POST.get('asientos')
        box_toura_add.description = request.POST.get('description')
        box_toura_add.code_paquet = request.POST.get('codepaquet')
        box_toura_add.price = request.POST.get('price')
        box_toura_add.dia = request.POST.get('fecha')
        box_toura_add.limites = request.POST.get('fechalimite')
        box_toura_add.value_cu = request.POST.get('valuecu')
        box_toura_add.photo = request.POST.get('img')
        box_toura_add.photo1_s  = request.POST.get('img1')
        box_toura_add.photo2_s  = request.POST.get('img2')
        box_toura_add.photo3_s  = request.POST.get('img3')
        box_toura_add.photo4_s  = request.POST.get('img4')
        box_toura_add.save()



    return render(request, 'app/admin_site/paque_tour.html', {'box_tours': box_tours})



# Esta vista eliminna los Box_Tours lo que son los paquetes de viajas
def delete_tours(request, paquet_tour_id):
    paque_delete = paquet_tour_id
    box_tours = Box_tours.objects.filter(id=paque_delete)
    if request.method == 'POST':
            
        box_tours.delete()
        return redirect('/paque_tour/')

    print('elimando paquete numero:', paque_delete)
    return render(request, 'app/admin_site/delete_tours.html',
                   {'box_tours': box_tours,})


# Esta vista crea los post o blogs
def blog_site(request):
    return render(request, 'apps/admin_site/blog_site.html')