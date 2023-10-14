from django.shortcuts import render

def home(request):
    return render(request, 'mainpage/home.html')

def about(request):
    return render(request, 'mainpage/about.html')

def portfolio(request):
    return render(request, 'mainpage/portfolio.html')

def contact(request):
    return render(request, 'mainpage/contact.html')
