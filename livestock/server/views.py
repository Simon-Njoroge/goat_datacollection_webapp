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

        return redirect('/admin/register/success/')

    return render(request, 'register_user.html')

def register_success(request):
    return render(request,'register_success.html')

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
                    return redirect('/admin/form/analyst/add/all/')
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

def livestock_form(request):
    return render(request,'livestock_form.html')


from django.shortcuts import redirect

from django.shortcuts import redirect
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def submit_livestock(request):
    if request.method == 'POST':
        # Handle form submission
        farmer_details = request.POST.get('farmer_details')  # Get the farmer details
        number_of_goats = request.POST.get('number_of_goats')
        male_goats = request.POST.get('male_goats')
        female_goats = request.POST.get('female_goats')
        goats_1_6_months = request.POST.get('goats_1_6_months')
        weight_1_7_kgs = request.POST.get('weight_1_7_kgs')
        weekly_goats_sold = request.POST.get('weekly_goats_sold')
        amount_paid_to_farmer = request.POST.get('amount_paid_to_farmer')
        date_sold = request.POST.get('date_sold')
        vaccination_schedule = request.POST.get('vaccination_schedule')
        deworming_schedule = request.POST.get('deworming_schedule')
        breeding_info = request.POST.get('breeding_info')
        traceability_system = request.POST.get('traceability_system')

        # Find the Farmer Details based on the provided ID
        try:
            farmer_details_instance = FarmersDetails.objects.get(id=farmer_details)
        except FarmersDetails.DoesNotExist:
            return HttpResponse("Farmer not found", status=400)

        # Create a new LivestockFarmer instance
        livestock_farmer = LivestockFarmer(
            farmer_details=farmer_details_instance,
            number_of_goats=number_of_goats,
            male_goats=male_goats,
            female_goats=female_goats,
            goats_1_6_months=goats_1_6_months,
            weight_1_7_kgs=weight_1_7_kgs,
            weekly_goats_sold=weekly_goats_sold,
            amount_paid_to_farmer=amount_paid_to_farmer,
            date_sold=date_sold,
            vaccination_schedule=vaccination_schedule,
            deworming_schedule=deworming_schedule,
            breeding_info=breeding_info,
            traceability_system=traceability_system
        )

        # Save the object to the database
        livestock_farmer.save()

        return HttpResponse("Form submitted successfully!")

    # Render the form if it's a GET request
    return render(request, 'livestock_form.html')


