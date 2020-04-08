
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import duffa
# Create your views here.
#function to render home page
def home(request):
    if request.method=="POST":
        uploaded_img=request.FILES["document"]
        s=duffa(name=uploaded_img.name,img=uploaded_img)
        s.save()
        
        return render(request,"new/submit.html")

    return render(request,"new/home.html")#code to render home page wit location as argument
