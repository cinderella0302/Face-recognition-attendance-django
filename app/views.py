from django.shortcuts import render



# Create your views here.
def Index(request):
    return render(request, 'app/index.html')

def Attend(request):
    return render(request, 'app/attend.html')