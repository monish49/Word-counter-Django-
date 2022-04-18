from django.shortcuts import render

def func(request):
    context={
        'var':'from second app',
        'name':'Varun',
        'age':23,
        'Address':'Banglore'

    }
    return render(request,'index.html',context)

# Create your views here.
