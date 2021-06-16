from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class User(AbstractUser):
	img= models.ImageField(upload_to='Profiles/',default="profile.png")
	dob=models.DateField(null=True)
	organization_name=models.CharField(max_length=120)
	hospital_name=models.CharField(max_length=120)
	g=[('Male','Male'),('Female','Female')]
	gender=models.CharField(max_length=10,choices=g)
	ph_no=models.CharField(max_length=10)
	pan_no=models.CharField(max_length=10)
	address=models.CharField(max_length=100)
	postal_code=models.CharField(max_length=7)
	city=models.CharField(max_length=20)
	state=models.CharField(max_length=20,default='Andra Pradesh')
	country=models.CharField(max_length=20,default='India')
	p=[(1,'Medicinist'),(2,'Organisation'),(3,'Guest')]
	role=models.IntegerField(choices=p,default=3)


class Rolrq(models.Model):
	r = [(1,'Medicinist'),(2,'Organisation')]
	uname = models.CharField(max_length=50)
	roltype = models.IntegerField(choices=r,default=0)
	prf = models.ImageField(upload_to='RolesRequested/')
	is_checked = models.BooleanField(default=0)
	ud = models.OneToOneField(User,on_delete=models.CASCADE)

class Orgdetails(models.Model):
	org_name=models.CharField(max_length=50,default="Organisation Name")
	found_name=models.CharField(max_length=50,default="Founder Name")
	est_date=models.DateField()
	us=models.OneToOneField(User,on_delete=models.CASCADE)

class MedicineInfo(models.Model):
	pharmacy_name=models.CharField(max_length=200)
	c=[('Tablet','Tablet'),('Syrup','Syrup'),('Injection','Injection')]
	medicine_name=models.CharField(max_length=120)
	category=models.CharField(choices=c,max_length=20,default="Tablet")
	dosage=models.CharField(max_length=20)
	days_count=models.CharField(max_length=20)
	production_date=models.DateField()
	entry_date=models.DateField()
	expiry_date=models.DateField()
	created_date=models.DateField(auto_now=True)
	quantity=models.CharField(max_length=20)
	remaining_tablets=models.CharField(max_length=20)
	uf=models.ForeignKey(User,on_delete=models.CASCADE)
	

class Organization(models.Model):
	r=[('request','Request'),('update','Update')]
	req=models.CharField(max_length=20,choices=r)
	org_name=models.CharField(max_length=200)
	orglicense_no=models.CharField(max_length=20)
	required_tablets=models.CharField(max_length=20)
	email=models.EmailField(max_length=120)
	oid=models.ForeignKey(User,on_delete=models.CASCADE)

class Donate(models.Model):
	donated_quantity=models.CharField(max_length=20)
	pomid=models.ForeignKey(MedicineInfo,on_delete=models.CASCADE)

class Export(models.Model):
	is_medicinist = models.BooleanField(default=False)
	#age = models.IntegerField(default=10)
	u = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def createpf(sender,instance,created,**kwargs):
	if created:
		Export.objects.create(u=instance)
