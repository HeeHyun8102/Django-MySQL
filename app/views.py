from django.shortcuts import render

from .models import DoctorsMini

# Create your views here.
def index(request):
    doctors_list = DoctorsMini.objects.all()
    return render(request, 'index.html', {'doctors_list':doctors_list})

def final(request):
    doctorName = request.GET.get('doctor_name')
    doctorName_req = DoctorsMini.objects.filter(id=doctorName)
    context = {'doctorName':doctorName_req}
    return render(request,'index.html',context)