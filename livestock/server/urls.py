from django.urls import path
from django.shortcuts import render
from . import views
urlpatterns = [
   path('auth/register/', views.register_user, name='register_user'),
   path('register/success/', views.register_success, name='register_success'),
   path('view_users/', views.view_users, name='view_users'),
   path('auth/login/', views.login_user, name='login_user'),
   path('logout/', views.user_logout, name='logout_user'),
   path('site/dashboard/dashboard/',views.adminHome,name='admin'),
   path('all/site/livestock/', views.livestock_farmers, name='livestock_farmers'),
   path('all/site/registered_farmers/', views.registered_farmers, name='registered_farmers'),
   path('all/site/fodder/',views.fodderFarmers,name='fodder_farmers_list'),
   path('all/site/infrastructure/',views.infrastructure,name='infrastructure'),
   path('all/site/capacitybuilding/',views.capacityBuilding,name='capacity_building_list'),
   path('new/form/add_farmer/', views.farmer_form, name='add_farmer'),
   path('new/add-farmer/', views.add_farmer, name='add_farmer'),
   path('new/add/farmer/success/', lambda request: render(request, 'success.html'), name='success_page'),
   path('form/analyst/add/all/', views.livestock_form, name='livestock_form'),
   # path('analyst/submit-livestock/', views.submit_livestock, name='submit_livestock')
]
