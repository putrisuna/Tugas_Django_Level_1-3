from django.shortcuts import render
from django.http import HttpResponse
from wishes.models import Topic, Webpage, AccesRecord
# Create your views here.
def index(request):
    webpages_list = AccesRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'wishes/index.html', context=date_dict)
