from django.db import models

# # Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
class CustomUser(models.Model):
    ADMIN = 'admin'
    ANALYST = 'analyst'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (ANALYST, 'Analyst'),
    ]

   
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # Store hashed password
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ANALYST)

    def set_password(self, raw_password):
        """Hashes the password before saving"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Checks if the given password matches the hashed password"""
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
    
class FarmersDetails(models.Model):
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    date_joined=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class LivestockFarmer(models.Model):
    farmer_details = models.ForeignKey(FarmersDetails, on_delete=models.CASCADE)
    number_of_goats = models.IntegerField()
    male_goats = models.IntegerField()
    female_goats = models.IntegerField()
    goats_1_6_months = models.IntegerField()
    weight_1_7_kgs = models.IntegerField()
    weekly_goats_sold = models.IntegerField()
    amount_paid_to_farmer = models.DecimalField(max_digits=10, decimal_places=2)
    date_sold = models.DateField()
    vaccination_schedule = models.TextField()
    deworming_schedule = models.DateField()
    breeding_info = models.TextField()
    traceability_system = models.TextField()
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.farmer_details.name



class FodderFarmer(models.Model):
    farmer_details = models.ForeignKey(FarmersDetails, on_delete=models.CASCADE)
    land_acreage_for_fodder = models.FloatField()
    leased = models.BooleanField()
    sharing_model = models.TextField()
    groups_associated = models.CharField(max_length=255)
    group_members_count = models.IntegerField()
    total_hectares_under_pastures = models.FloatField()
    yield_per_harvest = models.FloatField()
    region = models.CharField(max_length=255)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.farmer_details.name






class CapacityBuilding(models.Model):
    number_of_trainings = models.IntegerField()
    number_of_people_trained = models.IntegerField()
    modules_covered = models.TextField()
    region = models.CharField(max_length=255)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Capacity Building in {self.region}"


class Infrastructure(models.Model):
    location = models.CharField(max_length=255, db_index=True)
    water_used = models.FloatField(default=0.0)
    people_using_water = models.PositiveIntegerField(default=0)
    livestock_using_water = models.PositiveIntegerField(default=0) 
    bales_stored = models.PositiveIntegerField(default=0)
    hay_size = models.FloatField(default=0.0)
    bales_given_or_sold = models.PositiveIntegerField(default=0)
    revenue_made = models.FloatField(default=0.0)
    region = models.CharField(max_length=255)

    def _str_(self):
        return self.location







class FarmerRelationship(models.Model):
    livestock_farmer = models.ForeignKey(LivestockFarmer, on_delete=models.CASCADE)
    fodder_farmer = models.ForeignKey(FodderFarmer, on_delete=models.CASCADE)
    relationship_type = models.CharField(max_length=255)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.livestock_farmer.farmer_details.name} - {self.fodder_farmer.farmer_details.name}"


class FarmerInfrastructure(models.Model):
    livestock_farmer = models.ForeignKey(LivestockFarmer, on_delete=models.CASCADE)
    borehole = models.ForeignKey(Infrastructure, on_delete=models.SET_NULL, null=True, blank=True)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Infrastructure for {self.livestock_farmer.farmer_details.name}"
