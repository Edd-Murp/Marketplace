from django.shortcuts import render

#Home
def home(request):
    context = {'nome': 'Eduardo'}
    return render(request, "pages/home.html", context)

#About
def about(request):
    return render(request, "pages/aboutme.html")