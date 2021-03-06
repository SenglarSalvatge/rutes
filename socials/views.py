from django.shortcuts import render
from socials.forms import ComentariForm
from django.contrib import messages
from socials.models import Comentari
from posts.models import Post
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

# Create your views here.
def finalComentari(request):
    return render(request, 'socials/graciesComentari.html')

def entrarComentaris(request,id_ruta,id_comentari = None):
    if id_comentari is None:
        comentari = Comentari()
    else:
        comentari = Comentari.objects.get(pk = id_comentari) 
     
    if request.method == 'POST':
        form = ComentariForm(request.POST, instance = comentari)
        if form.is_valid():
            s = form.save(commit = False)
            user_perfil = request.user.perfil
            user_ruta = Post.objects.get(pk = id_ruta)
            s.perfil = user_perfil
            s.post = user_ruta
            s.save()
            messages.success(request, 'Comentari entrat correctament')
            url_next = reverse('socials:finalComentari')            
            return HttpResponseRedirect( url_next )
        else:
            messages.error(request, 'Error')            
    else: 
        form = ComentariForm(instance = comentari)

    return render(request, 'socials/entrarComentaris.html', {'form':form, 'ruta':id_ruta})

def llistarComentaris(request):
    return render(request, 'socials/llistarComentaris.html')