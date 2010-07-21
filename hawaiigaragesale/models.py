from appengine_django.models import BaseModel
from google.appengine.ext import db

# Create your models here.
class GarageSale(BaseModel):
    address = db.StringProperty()
    sale_date = db.DateProperty('garage sale date')
    contact_name = db.StringProperty()
    contract_phone = db.StringProperty()

