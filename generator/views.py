from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = [chr(i) for i in range(ord('a'),ord('z')+1)]+[chr(i) for i in range(ord('0'),ord('9')+1)]+['!','@','#','$','%','^','&','*']
    lenght = 10
    value = ''
    for i in range(lenght):
        value += random.choice(characters)
    return render(request, 'generator/password.html',{'password':value,'title': 'password page'})