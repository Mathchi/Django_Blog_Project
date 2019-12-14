from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "numbers": [1,2,3,4,5]
    }
    return render(request,"index.html", context)

def about(request):
    return render(request, "about.html")
