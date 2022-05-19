from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from .models import Etudiant


def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def admin(request):
    template = loader.get_template('administration.html')
    return HttpResponse(template.render())


def etudian(request):
    mystudent = Etudiant.objects.all().values()
    template = loader.get_template('index2.html')
    context = {
        'mystudent': mystudent,
    }

    return HttpResponse(template.render(context, request))


def administration(request):
    template = loader.get_template('administration.html')
    return HttpResponse(template.render())


def prof(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index1.html')
    context = {
        'mymembers': mymembers,
    }

    return HttpResponse(template.render(context, request))


def username(request):
    template = loader.get_template('username.html')
    return HttpResponse(template.render())


def pf(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }

    return HttpResponse(template.render(context, request))


@login_required
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


@login_required
def addrecord(request):
    x = request.POST['batiment']
    y = request.POST['nbr']
    member = Members(batiment=x, nbr=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))


@login_required
def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


@login_required
def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


@login_required
def updaterecord(request, id):
    batiment = request.POST['batiment']
    nbr = request.POST['nbr']
    member = Members.objects.get(id=id)
    member.batiment = batiment
    member.nbr = nbr
    member.save()
    return HttpResponseRedirect(reverse('index'))


def pe(request):
    mystudent = Etudiant.objects.all().values()
    template = loader.get_template('indexst.html')
    context = {
        'mystudent': mystudent,
    }

    return HttpResponse(template.render(context, request))


@login_required
def addst(request):
    template = loader.get_template('addst.html')
    return HttpResponse(template.render({}, request))


@login_required
def addrecordst(request):
    z = request.POST['batiment']
    t = request.POST['nbre']
    stu = Etudiant(batiment=z, nbre=t)
    stu.save()
    return HttpResponseRedirect(reverse('index'))


@login_required
def deletest(request, id):
    stu = Etudiant.objects.get(id=id)
    stu.delete()
    return HttpResponseRedirect(reverse('index'))


@login_required
def updatest(request, id):
    mystudent = Etudiant.objects.get(id=id)
    template = loader.get_template('updatest.html')
    context = {
        'mystudent': mystudent,
    }
    return HttpResponse(template.render(context, request))


@login_required
def updaterecordst(request, id):
    batiment = request.POST['batiment']
    nbre = request.POST['nbre']
    stu = Etudiant.objects.get(id=id)
    stu.batiment = batiment
    stu.nbre = nbre
    stu.save()
    return HttpResponseRedirect(reverse('index'))
