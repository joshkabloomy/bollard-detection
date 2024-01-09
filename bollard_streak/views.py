from django.shortcuts import render
from .models import CountryStreak
import random
from .forms import CheckCountry
from django.http import HttpResponse

def bollard_streak(request):
    # Session
    counter = request.session.get('counter', 0)
    
    # Fetch image from sql database
    table_size = CountryStreak.objects.last().pk
    
    if 'prev_pk' in request.session:
        prev_pk = request.session['prev_pk']
        prev = CountryStreak.objects.get(pk=prev_pk)
    else:
        prev_pk = random.randint(1, table_size)
        prev = None


    r = prev_pk
    data = CountryStreak.objects.get(pk=r)
    print(data.countries)
    
    correct = False
    country = ""
    if request.method == 'POST':
        print(request.POST)
        form = CheckCountry(request.POST)
        if form.is_valid():
            word_to_check = form.cleaned_data['word_to_check']
            word_to_check = word_to_check.lower()
            if word_to_check == "us" or word_to_check == "usa" or word_to_check == "u.s.a.":
                word_to_check = "united states"
            elif word_to_check == "uk":
                word_to_check = "united kingdom"
            print(word_to_check + " | " + prev.countries)
            country = prev.countries
            lower_case_country = country.lower() #lowercase input
            arr = lower_case_country.split(",")
            arr = [x.strip(" ") for x in arr]
            if word_to_check.lower() in arr:
                counter += 1
                request.session['counter'] = counter
                correct = True
                r = random.randint(1, table_size)
                data = CountryStreak.objects.get(pk=r)
            else:
                endstreak = counter
                request.session['best_streak'] = max(request.session.get('best_streak',0), endstreak)
                best_streak = request.session.get('best_streak')
                request.session['counter'] = 0
                request.session['prev_pk'] = random.randint(1, table_size)
                correct = False
                return render(request, 'bollard_streak/incorrect.html', {'data': prev, 'form': form, 'correct': correct, 'country': country, 'counter': endstreak, 'best_streak': best_streak})
    else:
        form = CheckCountry()
    
    request.session['prev_pk'] = r # saves the last primary key
    best_streak = max(request.session.get('best_streak',0), counter)
    return render(request, 'bollard_streak/country_streak.html', {'data': data, 'form': form, 'correct': correct, 'country': country, 'counter': counter, 'best_streak': best_streak})







    