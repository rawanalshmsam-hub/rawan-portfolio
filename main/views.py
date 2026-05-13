from django.shortcuts import render

# Create your views here.

def Home(request):

    return render (request,'main/home.html')



def about (request):
    return render(request,'main/about.html')

def works(request):
    return render(request,'main/works.html')

def contan(request):
    return render(request,'main/contact.html')


def achiev(request):
    return render(request,'main/achievements.html')








