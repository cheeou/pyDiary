from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PageForm
from .models import Page
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


class PageListView(View):
    def get(self, request):
        page_list = Page.objects.order_by("-page_date")
        return render(request, "diary/page_list.html", {"page_list": page_list})


class PageDetailView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_detail.html", {"page": page})


index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
