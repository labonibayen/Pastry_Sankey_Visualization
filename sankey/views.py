from __future__ import unicode_literals
from .models import DataPoint
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.forms.models import model_to_dict
import json
import csv
import codecs
from django.shortcuts import render
from django.core import serializers



def sankeydiagram(request):
	rows = serializers.serialize("json", DataPoint.objects.filter(in_sankey = True))
	return render(request, 'sankey/index.html', {'rows':rows})
