from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'About.html')

def Services(request):
    return render(request, 'Services.html')

def Pricing(request):
    return render(request, 'Pricing.html')

def Cars(request):
    return render(request, 'Cars.html')

def Blog(request):
    return render(request, 'Blog.html')

def Contact(request):
    return render(request, 'Contact.html')

