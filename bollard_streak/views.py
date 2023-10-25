from django.shortcuts import render
from .models import CountryStreak
import random
from .forms import CheckCountry
from django.http import HttpResponse

prev = ""
counter = 0
def bollard_streak(request):
    global counter
    global prev
    table_size = CountryStreak.objects.last().pk
    r = random.randint(1, table_size) 
    data = CountryStreak.objects.get(pk=r)
    print(data.countries)

    #check_country(request)
    correct = False
    country = ""
    if request.method == 'POST':
        print("send help")
        form = CheckCountry(request.POST)
        if form.is_valid():
            word_to_check = form.cleaned_data['word_to_check']
            print(word_to_check + "  " + prev.countries)
            country = prev.countries
            lower_case_country = country.lower() #lowercase input
            arr = lower_case_country.split(",")
            if word_to_check.lower() in arr:
                counter += 1
                correct = True
            else:
                endstreak = counter
                counter = 0
                correct = False
                return render(request, 'bollard_streak/incorrect.html', {'data': prev, 'form': form, 'correct': correct, 'country': country, 'counter': endstreak})
    else:
        form = CheckCountry()
    prev = data
    return render(request, 'bollard_streak/country_streak.html', {'data': data, 'form': form, 'correct': correct, 'country': country, 'counter': counter})

# def check_country(request):
#     print(request.method)
#     if request.method == 'POST':
#         form = CheckCountry(request.POST)
#         if form.is_valid():
#             word_to_check = form.cleaned_data['word_to_check']
#             if word_to_check == data.countries:
#                 print("Correct")
#                 return HttpResponse("Word matches the value.")
#             else:
#                 return HttpResponse("Word does not match the value.")
#     else:
#         form = CheckCountry()

#     return render(request, 'bollard_streak/country_streak.html', {'form': form})





    