from django.db import models







class PersonalDetail(models.Model):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    other_name = models.CharField(max_length=254, null=True, blank=True)
    id_date_of_birth = models.DateField(null=True, blank=True)
    id_id_number = models.CharField(max_length=254, null=True, blank=True)
    id_kra_pin = models.CharField(max_length=254, null=True, blank=True)
    id_gender = models.CharField(max_length=254, null=True, blank=True)
    id_Nationality = models.TextField(max_length=254, null=True, blank=True)
    id_town = models.TextField()
    id_mobile_number = models.CharField(max_length=300)
    id_county= models.CharField(max_length=300)
    id_marital_status = models.CharField(max_length=300)
    nssf_number= models.IntegerField(default=0)
    id_county= models.CharField(max_length=300)
    id_disabledStatus = models.CharField(max_length=254, null=True, blank=True)
    id_description = models.CharField(max_length=254, null=True, blank=True)
     


    
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()






