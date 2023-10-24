from django.shortcuts import render

def bollard_streak(request):
    return render(request, 'bollard_streak/game.html')