from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import json




# Create your views here.
def home(request):
    return render(request,'covidapp/home.html')

def stats(request):
    url1='https://covid-193.p.rapidapi.com/statistics'
    pmtr1 = {'country':'India'}
    headers1 = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "2a3b15c6f1mshe3a9940adbcd05dp19ab89jsna95e11818f1f"
    }

    response1 = requests.get(url1,params=pmtr1,headers=headers1)
    modified_response1 = response1.json()
    dict_response1 = modified_response1['response']
    final_response_india = dict_response1[0]

    Deaths_India=final_response_india['deaths']

    Cases_India = final_response_india['cases']

    Recovered_India =Cases_India['recovered']


    #India_df = pd.DataFrame(list(zip(Provinces_china,Confirmed_china,Deaths_china,Recovered_china)))
    return render(request,'covidapp/stats.html',{'Total_Cases_India':Cases_India['total'],'Active_cases':Cases_India['active'],'Deaths_India':Deaths_India['total'],'New_deaths_india_today':Deaths_India['new'],'Recovered_India':Recovered_India})


def intstats(request):
    url='https://covid-193.p.rapidapi.com/statistics'
    pmtr = {'country':'China'}
    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "2a3b15c6f1mshe3a9940adbcd05dp19ab89jsna95e11818f1f"
    }

    response = requests.get(url,params=pmtr,headers=headers)
    modified_response = response.json()
    dict_response = modified_response['response']
    final_response_china = dict_response[0]

    Deaths_china=final_response_china['deaths']

    Cases_China = final_response_china['cases']

    Recovered_China =Cases_China['recovered']

    #China_df = pd.DataFrame(list(zip(Provinces_china,Confirmed_china,Deaths_china,Recovered_china)))
    return render(request,'covidapp/intstats.html',{'Total_cases_China':Cases_China['total'],'Active_cases':Cases_China['active'],'Critical_cases':Cases_China['critical'],'new_cases_china':Cases_China['new'],'New_deaths_China_today':Deaths_china['new'],'Total_deaths_China':Deaths_china['total'],'Recovered_china':Recovered_China})
