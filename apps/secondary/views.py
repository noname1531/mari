from django.shortcuts import render
from apps.settings.models import Settings,Video,Services
from apps.secondary.models import About,News,Gallery,List
from apps.team.models import Team
# Create your views here.
# def about(request):
#     video = Video.objects.latest('id')
#     services = Services.objects.all()
#     setting = Settings.objects.latest('id')
#     about = About.objects.latest('id')
#     team = Team.objects.all()
#     return render(request, 'about.html')

# def news(request):
#     setting = Settings.objects.latest('id')
#     news = News.objects.all()
#     return render(request, 'news.html', locals())

# def news_detail(request,id):
#     setting = Settings.objects.latest('id')
#     news = News.objects.get(id=id)
#     return render(request,'post.html', locals())

# def gallery(request):
#     setting = Settings.objects.latest('id')
#     gallery = Gallery.objects.all()
#     return render(request, 'gallery.html', locals())

# def list(request):
#     setting = Settings.objects.latest('id')
#     list = List.objects.latest('id')
#     return render(request, 'list.html', locals())