from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from sdks.ecom.utility import fetch_pincodes
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class add_pincodes(LoginRequiredMixin, View):

    def get(self, reqest):

        fetch_pincodes()

        return JsonResponse({"goAhead":True})

