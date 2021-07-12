from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snack
# Create your views here.


class SnacksList(ListView):
    template_name = 'snack-list.html'
    model = Snack


class SnacksDetail(DetailView):
    template_name = 'snack-detail.html'
    model = Snack
