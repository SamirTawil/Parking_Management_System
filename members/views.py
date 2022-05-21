from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import MyUser, ParkingSpot

prof_parking_per_building = 50
student_parking_per_building = 100


# @user_passes_test(user_is_prof, login_url="login")   PROF
# @user_passes_test(user_is_student, login_url="login")   STUDENT


def user_is_prof(user):
    return user.role == "Professor"


def user_is_student(user):
    return user.role == "Student"


def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def admin(request):
    template = loader.get_template('administration.html')
    return HttpResponse(template.render())


def etudian(request):
    # mystudent = Etudiant.objects.all().values()
    mystudent = MyUser.objects.filter(role="Student").values()
    template = loader.get_template('index2.html')
    context = {
        'mystudent': mystudent,
    }

    return HttpResponse(template.render(context, request))


def administration(request):
    template = loader.get_template('administration.html')
    return HttpResponse(template.render())


def prof(request):
    mymembers = MyUser.objects.filter(role="Professor").values()
    template = loader.get_template('index1.html')
    context = {
        'mymembers': mymembers,
    }

    return HttpResponse(template.render(context, request))


def username(request):
    template = loader.get_template('username.html')
    return HttpResponse(template.render())


def pf(request):
    mymembers = MyUser.objects.filter(role="Professor").values()
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
    # member = Members(batiment=x, nbr=y)
    member = MyUser(role="Professor", current_spot_id=ParkingSpot.objects.create(batiment=x, nbr=y).id)
    member.save()
    return HttpResponseRedirect(reverse('index'))


@login_required
def delete(request, id):
    # member = Members.objects.get(id=id)
    member = MyUser.objects.get(role="Professor", id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


@login_required
def update(request, id):
    # mymember = Members.objects.get(id=id)
    mymember = MyUser.objects.get(role="Professor", id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


@login_required
def updaterecord(request, id):
    batiment = request.POST['batiment']
    nbr = request.POST['nbr']
    # member = Members.objects.get(id=id)
    member = MyUser.objects.get(role="Professor", id=id)
    member.batiment = batiment
    member.nbr = nbr
    member.save()
    return HttpResponseRedirect(reverse('index'))


def pe(request):
    # mystudent = Etudiant.objects.all().values()
    mystudent = MyUser.objects.filter(role="Student").values()
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
    # stu = Etudiant(batiment=z, nbre=t)
    stu = MyUser(role="Student", current_spot_id=ParkingSpot.objects.create(batiment=z, nbre=t).id)
    stu.save()
    return HttpResponseRedirect(reverse('index'))


@login_required
def deletest(request, id):
    # stu = Etudiant.objects.get(id=id)
    stu = MyUser.objects.get(id=id, role="Student")
    stu.delete()
    return HttpResponseRedirect(reverse('index'))


@login_required
def updatest(request, id):
    # mystudent = Etudiant.objects.get(id=id)
    mystudent = MyUser.objects.get(id=id, role="Student")
    template = loader.get_template('updatest.html')
    context = {
        'mystudent': mystudent,
    }
    return HttpResponse(template.render(context, request))


@login_required
def updaterecordst(request, id):
    batiment = request.POST['batiment']
    nbre = request.POST['nbre']
    # stu = Etudiant.objects.get(id=id)
    stu = MyUser.objects.get(id=id, role="Student")
    stu.batiment = batiment
    stu.nbre = nbre
    stu.save()
    return HttpResponseRedirect(reverse('index'))


def remaining_student_spots(batiment):
    taken_spots = ParkingSpot.objects.filter(batiment=batiment, user__role="Student")
    return student_parking_per_building - len(taken_spots)


def remaining_prof_spots(batiment):
    taken_spots = ParkingSpot.objects.filter(batiment=batiment, user__role="Professor")
    return prof_parking_per_building - len(taken_spots)
