from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image


# Create your views here.
def home(request):
    return render(request,'covidapp/home.html')

def stats(request):
    url = 'https://www.covidout.in'
    page = requests.get(url)
    soup_obj = BeautifulSoup(page.content,'html.parser')
    output = soup_obj.findAll('h2',{'class':'case'})

    numbers = []

    for i in output:
        numbers.append(i.text)

    Confirmed_cases = numbers[0]
    Hospitalized_cases = numbers[1]
    Intensive_care_cases = numbers[2]
    Recovered_cases = numbers[3]
    Deaths = numbers[4]

    for i in range(0,len(numbers)):
        numbers[i] = int(numbers[i])
        
    details = ['Confirmed_cases','Hospitalized_cases','Intensive_care_cases','Recovered_cases','Deaths']

    return render(request,'covidapp/stats.html',{'Confirmed_cases':Confirmed_cases,'Hospitalized_cases':Hospitalized_cases,'Intensive_care_cases':Intensive_care_cases,'Recovered_cases':Recovered_cases,'Deaths':Deaths})
