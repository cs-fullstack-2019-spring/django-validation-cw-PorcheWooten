from django.shortcuts import render
from django.http import HttpResponse
from .forms import CarForm
from .models import NewCar


# Creates form
def index(request):
    form = CarForm() #asign model and form to a variable
    NewCarModel = NewCar.objects.all()

    if request.method == "POST":
      form = CarForm(request.POST)
    if (form.is_valid()):
        NewCar.objects.create(make= request.POST['make'],model=request.POST['model'],
                                   year=request.POST['year'],mpg=request.POST['mpg'])
        #this adds the car and makes it an actual model
        return render(request,'carApp/congratulations.html',)
        #this renders the congratulations page
    else:
        context= {
                "form":CarForm,
                'model': NewCar,  #this adds errors for rendering the page
                'errors':CarForm.errors
            }
        return render(request,'carApp/index.html',context)


# access to the congratulations.html
def congrats(request):
    return render(request,'carApp/congrats.html',)