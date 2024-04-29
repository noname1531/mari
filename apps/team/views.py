from django.shortcuts import render
from apps.settings.models import Settings
# from apps.team.models import Team,Founder
# Create your views here.
# def team(request):
#     setting = Settings.objects.latest('id')
#     team = Team.objects.all()
#     founder = Founder.objects.latest('id')
#     return render(request, 'team.html', locals())