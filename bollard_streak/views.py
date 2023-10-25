from django.shortcuts import render
from .models import CountryStreak
import random
from .forms import CheckCountry
from django.http import HttpResponse

def bollard_streak(request):
    table_size = CountryStreak.objects.last().pk
    r = random.randint(1, table_size) 
    data = CountryStreak.objects.get(pk=r)
    print(data.countries)

    #check_country(request)
    correct = False
    if request.method == 'POST':
        form = CheckCountry(request.POST)
        if form.is_valid():
            word_to_check = form.cleaned_data['word_to_check']
            print(word_to_check + "  " + data.countries)
            if word_to_check == data.countries:
                print("Correct")
                correct = True
            else:
                correct = False
    else:
        form = CheckCountry()

    return render(request, 'bollard_streak/country_streak.html', {'data': data, 'form': form, 'correct': correct})

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





    
