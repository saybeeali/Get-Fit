from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
# from .models import Workout
from .models import Bodypart
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
            return redirect("artist_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class About(TemplateView):
    template_name = "about.html"



# @method_decorator(login_required, name='dispatch')
# class WorkoutList(TemplateView):
#     template_name = 'workout_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # to get the query parameter we have to acccess it in the request.GET dictionary object        
#         name = self.request.GET.get("name")
#         # If a query exists we will filter by name 
#         if name != None:
#             # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
#             context["workouts"] = Workout.objects.filter(name__icontains=name)
#         else:
#             context["workouts"] = Workout.objects.all()
#         return context



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

class BodypartUpdate(UpdateView):
    model = Bodypart
    fields = ['name', 'img', 'Benefits']
    template_name ='workout_create.html'
    success_url = '/workouts/'

class BodypartDelete(DeleteView):
    model = Bodypart
    template_name = 'workout_delete_confirmation.html'
    success_url = '/workouts/'