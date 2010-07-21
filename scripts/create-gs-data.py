from hawaiigaragesale.models import GarageSale
import time
from datetime import date
from datetime import timedelta


##########################
## To run, do:
## python manage.py  shell < scripts/create-gs-data.py 
##########################

gs = GarageSale(address="940 Spencer St, Honolulu, HI ", sale_date=date.today() + timedelta(days=1) ,contact_name='Kevin English',contract_phone='808-271-5125')
gs.save()
gs = GarageSale(address="900 Fort Street Mall, Honolulu, HI ",sale_date=date.today() + timedelta(days=2),contact_name='Kevin English',contract_phone='808-271-5125')
gs.save()
gs = GarageSale(address="241 Kaiulani Ave, Honolulu, HI ", sale_date=date.today() + timedelta(days=3),contact_name='Kevin English',contract_phone='808-271-5125')
gs.save()
gs = GarageSale(address="91-1031 Kaimalie St, Ewa Beach, HI ", sale_date=date.today() + timedelta(days=4),contact_name='Kevin English',contract_phone='808-271-5125')
gs.save()

gs = GarageSale(address="1001 Bishop St, Honolulu, HI ", sale_date=date.today() + timedelta(days=5),contact_name='Kevin English',contract_phone='808-271-5125')
gs.save()

