from hawaiigaragesale.models import GarageSale
import time
from datetime import date


##########################
## To run, do:
## python manage.py  shell < scripts/create-gs-data.py 
##########################

#gs = GarageSale(address="940 Spencer St, Honolulu, HI ", sale_date=date.today(),contact_name='Kevin English',contract_phone='808-271-5125')
#gs.save()
gs = GarageSale(address="900 Fort Street Mall, Honolulu, HI ", sale_date=date.today(),contact_name='Kevin English',contract_phone='808-271-5125')
gs.save()
#gs = GarageSale(address="241 Kaiulani Ave, Honolulu, HI ", sale_date=date.today(),contact_name='Kevin English',contract_phone='808-271-5125')
#gs.save()
#gs = GarageSale(address="91-1031 Kaimalie St, Ewa Beach, HI ", sale_date=date.today(),contact_name='Kevin English',contract_phone='808-271-5125')
#gs.save()

