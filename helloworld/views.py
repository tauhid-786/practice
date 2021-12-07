from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
developed_by="md tauhid alam"
mentors=["alam",
        "md",
        "ashar",
        "chirag"
]
context={"developer":developed_by,
"mentors":mentors}
def index(request):
    return render(request,'helloworld/index.html',context)
def home(request):
    return HttpResponse("i am at home")