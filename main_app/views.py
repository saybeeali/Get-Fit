from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
# from .models import Workout
from .models import Bodypart, Exercise, Routine
# login
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"




@method_decorator(login_required, name='dispatch')
class RoutineList(TemplateView):
    template_name = 'routine_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["routines"] = Routine.objects.all()
        return context




class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("workout_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class About(TemplateView):
    template_name = "about.html"




@method_decorator(login_required, name='dispatch')
class BodypartList(TemplateView):
    template_name = 'workout_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["bodyparts"] = Bodypart.objects.filter(name__icontains=name)
        else:
            context["bodyparts"] = Bodypart.objects.all()
        return context


class BodypartCreate(CreateView):
    model = Bodypart
    fields = ['name', 'img', 'Benefits']
    template_name ='workout_create.html'
    success_url = '/workouts/'

class BodypartDetail(DetailView):
    model = Bodypart
    template_name = 'workout_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["routines"] = Routine.objects.all()
        return context



class BodypartUpdate(UpdateView):
    model = Bodypart
    fields = ['name', 'img', 'Benefits']
    template_name ='workout_create.html'
    success_url = '/workouts/'

class BodypartDelete(DeleteView):
    model = Bodypart
    template_name = 'workout_delete_confirmation.html'
    success_url = '/workouts/'



class RoutineExerciseAssoc(View):

    def get(self, request, pk, exercise_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Routine.objects.get(pk=pk).exercises.remove(exercise_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Routine.objects.get(pk=pk).exercises.add(exercise_pk)
        return redirect('home')
