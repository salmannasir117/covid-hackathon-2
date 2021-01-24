from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta, timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def test_static(request):
     _file = open('static/tracker/wrapper.html').read()
     return render(request, 'tracker/test_static.html', {"HtmlFile": _file})
@login_required
def list_tests(request):
    #_list = Test.objects.filter(date__gte=datetime.now(timezone(timedelta(hours=-5)))-timedelta(weeks=3))
    _list = Test.objects.all()
#     person_tests = request.user.person.test_set.order_by('-date')
#     _list = Test.objects.filter(date__gte=datetime.now(timezone(timedelta(hours=-5)))-timedelta(weeks=52)).order_by('-date')
    return render(request, 'tracker/list_tests.html', {"test_list": _list,})
#     return render(request, 'tracker/list_tests.html', {"test_list": _list, "user_tests": person_tests})
