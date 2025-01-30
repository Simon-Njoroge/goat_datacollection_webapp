from django.shortcuts import render,redirect
from .models import LivestockFarmer,FodderFarmer,CapacityBuilding,FarmersDetails,FarmersDetails,CustomUser
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.utils import timezone

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role', 'analyst')  

        if CustomUser.objects.filter(username=username).exists():
            return HttpResponse("Username already exists", status=400)

       
        user = CustomUser(username=username, role=role)
        user.set_password(password)
        user.save()

        return redirect('register_success.html')

    return render(request, 'register_user.html')


def view_users(request):
    users = CustomUser.objects.all()
    return render(request, 'view_users.html', {'users': users})


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser  
from django.contrib.auth import authenticate, login

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                

                if user.role == 'analyst':
                    return redirect('analyst_dashboard')
                elif user.role == 'admin':
                    return redirect('/admin/site/dashboard/dashboard/')
                else:
                    return HttpResponse("Invalid role", status=403)
            else:
                return HttpResponse("Invalid password", status=401)
        except CustomUser.DoesNotExist:
            return HttpResponse("User not found", status=404)

    return render(request, 'login.html')

def user_logout(request):
    logout(request)  
    return redirect('/admin/auth/login/')

def adminHome(request):
    regfarmers = FarmersDetails.objects.all()
    total_farmers = regfarmers.count()
    farmers = LivestockFarmer.objects.all()
    totalfarmers=farmers.count()
    fodder_farmers = FodderFarmer.objects.all()
    totalfodder=fodder_farmers.count()
    return render(request,'index.html',{'total_farmers': total_farmers,'totalfarmers':totalfarmers,'totalfodder':totalfodder})

def landingpage(request):
    return render(request,'landingpage.html')

def registered_farmers(request):
    regfarmers = FarmersDetails.objects.all()
    return render(request, 'registered_farmers.html', {'regfarmers': regfarmers})

def livestock_farmers(request):
    farmers = LivestockFarmer.objects.all()
    return render(request, 'livestock.html', {'farmers': farmers})

def recent_livestock_data(request):
   
    today = timezone.now().date()
    livestock_data = livestock_data.objects.filter(date_collected=today)

    return render(request, 'index.html', {'livestock_data': livestock_data})

def fodderFarmers(request):
    fodder_farmers = FodderFarmer.objects.all()
    return render(request,'fodder.html',{'fodder_farmers': fodder_farmers})

def infrastructure(request):
    return render(request,'infrastructure.html')

def capacityBuilding(request):
    trainings = CapacityBuilding.objects.all()
    return render(request,'capacitybuilding.html',{'trainings':trainings})

def recent_capacity_data(request):
   
    today = timezone.now().date()
    capacity_data = capacityBuilding.objects.filter(date_collected=today)

    return render(request, 'index.html', {'capacity_data': capacity_data})

def farmer_form(request):
    return render(request,'add_farmers.html')

def add_farmer(request):
    if request.method == 'POST':
        name = request.POST['name']
        id_number = request.POST['id_number']
        phone_number = request.POST['phone_number']
        location = request.POST['location']

        farmer = FarmersDetails(
            name=name,
            id_number=id_number,
            phone_number=phone_number,
            location=location
        )
        farmer.save()

        return redirect('success_page') 

    return render(request, 'add_farmers.html')