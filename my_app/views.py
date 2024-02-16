from django.shortcuts import render,get_object_or_404
from .models import Slider,About,Services,Doctors

def index(request):
    slider=Slider.objects.all()
    about=About.objects.all()
    service=Services.objects.all()
    doctor=Doctors.objects.all()
    
    
        
    data ={
        'slider': slider,
        'about': about,
        'service': service,
        'doctor': doctor,
     

    }
    return render(request, 'my_app/index.html', context=data)

def about(request):
    slider=Slider.objects.all()
    about=About.objects.all()
    service=Services.objects.all()
    doctor=Doctors.objects.all()
    
    
        
    data ={
        'slider': slider,
        'about': about,
        'service': service,
        'doctor': doctor,
     

    }
    return render(request, 'my_app/about.html', context=data)

def blog(request):
    return render(request, 'my_app/blog.html')

def contact(request):
    return render(request, 'my_app/contact.html')

def doctors(request):
    doctor=Doctors.objects.all()
    data={
        'doctor': doctor
    }
    return render(request, 'my_app/Doctors.html', context=data)

def departament(request):
    return render(request, 'my_app/Department.html')

def main(request):
    return render(request, 'my_app/main.html')

def single(request):
    return render(request, 'my_app/single-blog.html')

def elements(request):
    return render(request, 'my_app/elements.html')

def showdoctor(request, pk):
    doc=get_object_or_404(Doctors,id=pk)
    data={
        'doc': doc
    }
    return render(request,'my_app/showdoc.html', context=data)
