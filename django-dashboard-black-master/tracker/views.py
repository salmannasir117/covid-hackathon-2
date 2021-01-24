from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta, timezone
from django.contrib.auth.decorators import login_required
import pandas as pd

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.urls import reverse

# Create your views here.
def test_static(request):
     _file = open('static/tracker/wrapper.html').read()
     return render(request, 'tracker/test_static.html', {"HtmlFile": _file})
@login_required
def list_tests(request):
    #_list = Test.objects.filter(date__gte=datetime.now(timezone(timedelta(hours=-5)))-timedelta(weeks=3))
#     _list = Test.objects.all()
     _list = [] 
#     person_tests = request.user.person.test_set.order_by('-date')
#     _list = Test.objects.filter(date__gte=datetime.now(timezone(timedelta(hours=-5)))-timedelta(weeks=52)).order_by('-date')
     return render(request, 'tracker/list_tests.html', {"test_list": _list,})
#     return render(request, 'tracker/list_tests.html', {"test_list": _list, "user_tests": person_tests})
def download_template(request):
     df = pd.DataFrame(data=[], columns=["id", "date/time", "is positive"])
     df.to_excel("user_data.xlsx")
     with open("user_data.xlsx", 'rb') as fh:
          response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
          response['Content-Disposition'] = 'inline; filename=' + "user_data.xlsx"
          return response




def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if not form.is_valid():
          #   handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('tracker:list-tests'))
    else:
        form = UploadFileForm()
    return render(request, 'tracker/upload.html', {'form': form})


def list_tests2(request):
     _list = Test.objects.all()
#     person_tests = request.user.person.test_set.order_by('-date')
#     _list = Test.objects.filter(date__gte=datetime.now(timezone(timedelta(hours=-5)))-timedelta(weeks=52)).order_by('-date')
     
     if request.POST.get('filter', False) == 'user_data':
          _list = request.user.person.test_set.order_by('-date')
     if request.POST.get('filter', False) == 'only_positive':
          _list = Test.objects.filter(is_positive=True).order_by('-date')
     if request.POST.get('filter', False) == 'last_month':
          _list = Test.objects.filter(date__gte=datetime.now(timezone(timedelta(hours=-5)))-timedelta(weeks=52)).order_by('-date')
     if request.POST.get('filter', False) == 'friend_group':
          _list = request.user.person.test_set.order_by('-date')
          if len(request.user.friend_group.all()) != 0:
               for friend in request.user.friend_group.all()[0].friends.all():
                    _list |= friend.person.test_set.order_by('-date')
     
     return render(request, 'tracker/list_tests.html', {"test_list": _list,})
#     return render(request, 'tracker/list_tests.html', {"test_list": _list, "user_tests": person_tests})





# def handle_uploaded_file(f):
#      df = pd.read_excel(open(f, 'rb'))

#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)