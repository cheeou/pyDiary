from django.shortcuts import render, redirect
from django.views import View
from .forms import PageForm
from datetime import datetime
from zoneinfo import ZoneInfo

# Create your views here.


class IndexView(View):
    def get(self, request):
        datetime_now = datetime.now(ZoneInfo("Asia/Seoul")).strftime(
            "%Y년%m월%d일 %H:%M:%S"
        )
        return render(request, "diary/index.html", {"datetime_now": datetime_now})


class PageCreateView(View):
    def get(self, request):
        form = PageForm()
        return render(request, "diary/page_form.html", {"form": form})

    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("diary:index")
        return render(request, "diary/page_form.html", {"form": form})


index = IndexView.as_view()
page_create = PageCreateView.as_view()
