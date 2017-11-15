from django.shortcuts import render
from datetime import datetime
from tracking.models import Track


def index(request):
    track = Track()
    track.title = 'Alguien ha entrado'
    track.observation = 'Agente agente, arrestelx pronto'
    track.tracked_on = datetime.now()
    track.save()

    tracked = Track.objects.all()

    return render(request, 'index.html', {'tracked': tracked})
