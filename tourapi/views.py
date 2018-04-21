from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timelda
import json

def return_response(params):
	response = HttpResponse(params, content_type="application/json")
	response['Access-Control-Allow-Origin'] = "*"
	response['Access-Control-Allow-Headers'] = "origin, x-requested-with, content-type"
	response['Access-Control-Allow-Methods'] = "PUT, GET, POST, DELETE, OPTIONS"
	return response


