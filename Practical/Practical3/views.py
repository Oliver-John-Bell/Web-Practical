# Practical3/views.py
from django.shortcuts import render
from django.http import HttpResponse

def counting_game(request, number):
    stars = [ '*' * i for i in range(1, number + 1) ]
    return render(request, 'Practical3/counting_game.html', {'stars': stars, 'number': number})

def download_stars(request, number):
    stars = [ '*' * i for i in range(1, number + 1) ]
    stars_content = "\n".join(stars)
    
    response = HttpResponse(stars_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="stars_{number}.txt"'
    
    return response
