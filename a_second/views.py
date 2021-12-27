from django.shortcuts import redirect, render
from .models import Clock
from .forms import ClockForm
import json
# Create your views here.
def clock(request):
    clock_query_set = Clock.objects.all()
    clock_list = list(clock_query_set.values())
   
    return render(request, "a_second/index2.html",{"data_json": json.dumps(clock_list)})

def input(request):
    if request.method == "POST":
        print(request.POST)
        form = Clock.objects.create(second=float(request.POST["second"]))
        form.save()
        return redirect("a_second:clock")
    else:
        form = ClockForm
    return render(request, "a_second/form.html", {"form": form})
