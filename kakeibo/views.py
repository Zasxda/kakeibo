from datetime import UTC, datetime

from django.shortcuts import render

from .models import Record


def post_list(request):
    if request.method == "POST":
        Record.objects.create(
            date=datetime.now(UTC).date(),
            income=request.POST.get("income"),
            outcome=request.POST.get("outcome"),
        )

    records = Record.objects.all()

    return render(
        request,
        "kakeibo/post_list.html",
        {
            "records": records,
        },
    )
