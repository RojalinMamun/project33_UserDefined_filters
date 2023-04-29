from django.shortcuts import render

# Create your views here.

def filters(request):
    d={'data': 'HElLo How ArE yOu'}
    return render(request,'filters.html',d)
