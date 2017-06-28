from django.shortcuts import render
from myweb.models import Users
from django.core import serializers

# Create your views here.
def index(request):
    results =   serializers.serialize('json',Users.objects.all())
    return render( request,'index.html',{'content':results} )