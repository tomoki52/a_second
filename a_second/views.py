from django.shortcuts import redirect, render
from .models import Clock
from .forms import ClockForm
import json
# Create your views here.
def clock(request):
    clock_query_set = Clock.objects.all()
    clock_list = list(clock_query_set.values())
   
    return render(request, "a_second/index.html",{"data_json": json.dumps(clock_list)})

def input(request):
    if request.method == "POST":
        form = ClockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("a_second:clock")
    else:
        form = ClockForm
    return render(request, "a_second/form.html", {"form": form})
