from django.shortcuts import render
from .models import CountryStreak
import random
from .forms import CheckCountry
from django.http import HttpResponse

#prev = ""
#counter = 0
def bollard_streak(request):
    #global counter
    #global prev

    # Session
    counter = request.session.get('counter', 0)
    if 'prev_pk' in request.session:
        prev_pk = request.session['prev_pk']
        prev = CountryStreak.objects.get(pk=prev_pk)
    else:
        prev = None


    # Fetch image from sql database
    table_size = CountryStreak.objects.last().pk
    r = random.randint(1, table_size) 
    data = CountryStreak.objects.get(pk=r)
    print(data.countries)
    
    correct = False
    country = ""
    if request.method == 'POST':
        print(request.POST)
        form = CheckCountry(request.POST)
        if form.is_valid():
            word_to_check = form.cleaned_data['word_to_check']
            print(word_to_check + " | " + prev.countries)
            country = prev.countries
            lower_case_country = country.lower() #lowercase input
            arr = lower_case_country.split(",")
            arr = [x.strip(" ") for x in arr]
            if word_to_check.lower() in arr:
                counter += 1
                request.session['counter'] = counter
                correct = True
            else:
                endstreak = counter
                request.session['counter'] = 0
                correct = False
                return render(request, 'bollard_streak/incorrect.html', {'data': prev, 'form': form, 'correct': correct, 'country': country, 'counter': endstreak})
    else:
        form = CheckCountry()
    
    request.session['prev_pk'] = r # saves the last primary key
    return render(request, 'bollard_streak/country_streak.html', {'data': data, 'form': form, 'correct': correct, 'country': country, 'counter': counter})







    