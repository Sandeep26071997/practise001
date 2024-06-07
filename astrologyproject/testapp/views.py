from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
# Create your views here.
def result_view(request):
    msg_list=[
        'The golden days ahead',
        'Better to sleep more time even in class room also....',
        'Tomorrow will be the best day of your life',
        'Tomorrow is the perfect day to propose ur girlfriend',
        'Verysoon you will get job'
    ]
    names_list=['sunny','mallika','kareena','katrina','deepika','Samantha','Sony','Alia','Sandeep','Srikanth']
    time=datetime.datetime.now()
    h=int(time.strftime('%H'))

    if h<12:
        s='Morning'
    elif h<16:
        s='Afternoon'
    elif h<21:
        s='Evening'
    else:
        s='Night'
    name=random.choice(names_list)
    msg=random.choice(msg_list)
    my_dict={'time':time,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/astrology.html',my_dict)