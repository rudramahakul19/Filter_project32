from django.shortcuts import render

# Create your views here.
import datetime

def filters(request):
    dt=datetime.datetime.now()
    d={'data':'This IS THe coNTain','dt':dt,'c':2,'p':2}

    return render(request,'filters.html',d)