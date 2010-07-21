# Create your views here.
# Create your views here.
from django.template import Context, loader
from hawaiigaragesale.models import GarageSale
from django.http import HttpResponse

def index(request):
  latest_garage_sales = GarageSale.objects.all().order('-sale_date')[:5]
  t = loader.get_template('hawaiigaragesale/index.html')
  c = Context({
    'latest_garage_sales': latest_garage_sales,
  })
  return HttpResponse(t.render(c))
