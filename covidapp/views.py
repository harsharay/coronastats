from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import json




# Create your views here.
def home(request):
    return render(request,'covidapp/home.html')

def stats(request):
    url = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise"
    response = requests.get(url)
    final_response = response.json()
    confirmed_cases_india = final_response['data']['total']['confirmed']

    Deaths_India=final_response['data']['total']['deaths']

    Active_Cases_India = final_response['data']['total']['active']

    Recovered_India =final_response['data']['total']['recovered']


    #India_df = pd.DataFrame(list(zip(Provinces_china,Confirmed_china,Deaths_china,Recovered_china)))
    return render(request,'covidapp/stats.html',{'Confirmed_cases_India':confirmed_cases_india,'Deaths_india':Deaths_India,'Active_cases_india':Active_Cases_India,'Recovered_cases_india':Recovered_India})


def intstats(request):
    def country_stat(country_1):
        url='https://covid-193.p.rapidapi.com/statistics'
        headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "2a3b15c6f1mshe3a9940adbcd05dp19ab89jsna95e11818f1f"
        }
        response = requests.get(url,params={"country":country_1},headers=headers)
        resp_2 = response.json()
        final_resp = resp_2['response']
        output = final_resp[0]
        return output
    #China data
    final_response_china = country_stat("China")
    Deaths_china=final_response_china['deaths']

    Cases_China = final_response_china['cases']

    Recovered_China =Cases_China['recovered']
    #------------------------------------------------------------
    #Italy Data
    final_response_italy = country_stat('Italy')
    Deaths_italy=final_response_italy['deaths']

    Cases_italy = final_response_italy['cases']

    Recovered_italy =Cases_italy['recovered']
    #------------------------------------------------------------
    #USA Data
    final_response_usa = country_stat('USA')
    Deaths_usa=final_response_usa['deaths']

    Cases_usa = final_response_usa['cases']

    Recovered_usa =Cases_usa['recovered']
    #------------------------------------------------------------
    #Spain Data
    final_response_spain = country_stat('Spain')
    Deaths_spain=final_response_spain['deaths']

    Cases_spain = final_response_spain['cases']

    Recovered_spain =Cases_spain['recovered']

    return render(request,'covidapp/intstats.html',{'Total_cases_China':Cases_China['total'],'Active_cases':Cases_China['active'],'Critical_cases':Cases_China['critical'],'new_cases_china':Cases_China['new'],'New_deaths_China_today':Deaths_china['new'],'Total_deaths_China':Deaths_china['total'],'Recovered_china':Recovered_China,'Total_cases_italy':Cases_italy['total'],'Active_cases_italy':Cases_italy['active'],'Critical_cases_taly':Cases_italy['critical'],'new_cases_italy':Cases_italy['new'],'New_deaths_italy_today':Deaths_italy['new'],'Total_deaths_italy':Deaths_italy['total'],'Recovered_italy':Recovered_italy,'Total_cases_usa':Cases_usa['total'],'Active_cases_usa':Cases_usa['active'],'Critical_cases_usa':Cases_usa['critical'],'new_cases_usa':Cases_usa['new'],'New_deaths_usa_today':Deaths_usa['new'],'Total_deaths_usa':Deaths_usa['total'],'Recovered_usa':Recovered_usa,'Total_cases_spain':Cases_spain['total'],'Active_cases_spain':Cases_spain['active'],'Critical_cases_spain':Cases_spain['critical'],'new_cases_spain':Cases_spain['new'],'New_deaths_spain_today':Deaths_spain['new'],'Total_deaths_spain':Deaths_spain['total'],'Recovered_spain':Recovered_spain})


def helpline(request):
    return render(request, 'covidapp/helplines.html')
