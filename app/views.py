from django.shortcuts import render

from .models import DoctorsMini, CatholicDoc, SeoulDoc, SkkuDoc

#Create your views here.
# def index(request):
#    doctors_list = CatholicDoc.objects.all()
# #    seoul_doctorName = SeoulDoc.objects.all()
# #    doctors_list = doctors_cat 
#    return render(request, 'index.html', {'doctors_list':doctors_list})

def final(request):
    doctorName = request.GET.get('doctor_name')
#    doctorName_req = DoctorsMini.objects.filter(id=doctorName)

    cath_doctorName = CatholicDoc.objects.filter(id=doctorName)
    seoul_doctorName = SeoulDoc.objects.filter(id=doctorName)
    skku_doctorName = SkkuDoc.objects.filter(id=doctorName)
    doc_all = cath_doctorName.union(seoul_doctorName, skku_doctorName)


    context = {'doctorName': doc_all}
    return render(request,'index.html',context)