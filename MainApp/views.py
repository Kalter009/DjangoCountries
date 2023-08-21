from django.shortcuts import render
import json
import string as st


# Create your views here.

with open('../countries-by-languages.json', "r", encoding="UTF-8") as file:
    countries = json.load(file)

def index(request):
    return render(request, 'index.html', context)

def countries_list(request, *args):
    context = {"countries" == countries,
               "title" == "Countries List",
               "alphabet" == st.ascii_uppercase
    }
    if args:
        return render(request, 'countries_list_by_letter.html', context)
    return render(request, 'countries_list.html', context)

def one_country(request, country_name):
    context = {"title" = country_name,
               "countries" = countries
    }
    return render(request, 'one_country.html', context)

