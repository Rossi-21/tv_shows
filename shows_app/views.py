from django.shortcuts import render, redirect
from django.contrib import messages
from shows_app.models import Show

def index(request):
    return render(request, "index.html")

def create_show(request):
        
        errors = Show.objects.validator(request.POST)

        if len(errors) > 0:
            
            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect ('/shows/new')
       
        else:
            
            title = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['release_date']
            description = request.POST['description']
            
            show = Show.objects.create(title = title, network = network, release_date = release_date, description = description)
            
            return redirect(f"/shows/{show.id}",show)

def display_show(request, id):
      context = {"show": Show.objects.get(id=id)}
      return render(request, "display_show.html", context) 

def display_all(request):
      context = {"shows": Show.objects.all()}
      return render(request, "landing.html", context)

def edit_show(request, id):
      context = {"show": Show.objects.get(id=id)}
      return render(request, "edit.html", context )

def update(request, id):
        errors = Show.objects.validator(request.POST)

        if len(errors) > 0:
            show = Show.objects.get(id=id)
            
            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect (f"/shows/{show.id}/edit", show)
       
        else:
        
            show = Show.objects.get(id=id)

            title = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['release_date']
            description = request.POST['description']

            show.title = title
            show.network = network
            show.release_date = release_date
            show.description = description

            show.save()

            return redirect(f"/shows/{show.id}",show)

def delete(request, id):
      
      show = Show.objects.get(id=id)
      show.delete()

      return redirect("/shows")
