from django.shortcuts import render
from datetime import datetime
from .models import Record

def post_list(request):
    records = Record.objects.all()

    if (request.method == "POST"):
        records = Record.objects.create(
            # date = request.POST.get("today"),
            date = datetime.now(),
            income = request.POST.get("income"),
            outcome = request.POST.get("outcome"),
        )

    return render(
        request,
        'kakeibo/post_list.html',
        {
            "records": records,
        }
    )
