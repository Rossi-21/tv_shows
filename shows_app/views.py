from django.shortcuts import render, redirect
from shows_app.models import Show

def index(request):
    return render(request, "index.html")

def create_show(request):
        
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        

        show = Show.objects.create(title = title, network = network, release_date = release_date, description = description)
        
        return redirect(f"/shows/{show.id}",show)

def display_show(request, id):
      context = {"show": Show.objects.get(id=id)}
      return render(request, "display_show.html", context) 


