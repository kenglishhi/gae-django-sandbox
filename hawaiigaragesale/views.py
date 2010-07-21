# Create your views here.
# Create your views here.
import time
import log
from datetime import date
today = date.today()

from django.template import Context, loader
from hawaiigaragesale.models import GarageSale
from django.http import HttpResponse

def index(request):
  upcoming_garage_sales = GarageSale.objects.all().filter("sale_date >=", date.today()).order('-sale_date')[:5]
  t = loader.get_template('hawaiigaragesale/index.html')
  log.debug("My Message") 
  log.debug("Array len is %s " % len(upcoming_garage_sales)  ) 
  c = Context({
    'upcoming_garage_sales': upcoming_garage_sales,
  })
  return HttpResponse(t.render(c))
