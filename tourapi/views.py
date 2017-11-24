from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from tourapi.models import *
from django.views.decorators.csrf import csrf_exempt
import json


def return_response(params):
	response = HttpResponse(params, content_type="application/json")
	response['Access-Control-Allow-Origin'] = "*"
	response['Access-Control-Allow-Headers'] = "origin, x-requested-with, content-type"
	response['Access-Control-Allow-Methods'] = "PUT, GET, POST, DELETE, OPTIONS"
	return response


def api_get_tourists(request):
	tourists = Tourist.objects.all().order_by('-full_name')
	tourists = [tourist.get_tourist_json() for tourist in tourists]
	return return_response(json.dumps(tourists, indent=4, default=str))


def api_get_single_tourist(request, tourist):
	try:
		tourist = Tourist.objects.get(pk=tourist)
		return return_response(json.dumps(tourist.get_tourist_json(), indent=4, default=str))
	except Tourist.DoesNotExist:
		error = [{"404":"Tourist Not Found"}]
		return return_response(json.dumps(error, indent=4, sort_keys=False))


@csrf_exempt
def api_register_tourist(request):
	if request.method == "POST":
		tourist = json.loads(request.body)
		print tourist

		tourist_obj = Tourist(
				full_name = tourist["full_name"],
				email = tourist["email"]
			)
		tourist_obj.save()
		return return_response("Tourist Added !!!")
	else:
		error = [{"Fields":"full_name, email", "Error":"Expecting POST REQUEST", "Format":"json"}]
		return return_response(json.dumps(error, indent=4, sort_keys=True))


@csrf_exempt
def api_register_tourism(request):
	if request.method == "POST":
		tourism = json.loads(request.body)
		tourism_obj = Tourism(
				tourist = Tourist.objects.get(email=tourism["email"]),
				origin = tourism["origin"],
				destination = tourism["destination"],
				is_private = tourism["is_private"],
				date = datetime.now()
			)
		tourism_obj.save()
		return return_response("Tourism Added !!!")

	else:
		error = [{"Fields":"email, origin, destination, is_private(boolean)", "Error":"Expecting POST REQUEST", "Format":"json"}]
		return return_response(json.dumps(error, indent=4, sort_keys=True))


@csrf_exempt
def get_tourist_tourisms(request, tourist):
	if request.method == "POST":
		tourist_data = json.loads(request.body)
		print tourist_data
		try:
			tourist_obj = Tourist.objects.get(email=tourist_data["email"])

			if tourist_obj.pk == tourist:

				tourisms = Tourism.objects.filter(tourist=tourist).order_by('-date')
				tourisms = [tourism.get_tourism_json() for tourism in tourisms]
				return return_response(json.dumps(tourisms), indent=4, sort_keys=False)

			else:
				error = [{"401":"Not Authorized"}]
				return return_response(json.dumps(error, indent=4, sort_keys=False))

		except Tourist.DoesNotExist:

			error = [{"404":"Tourist Not Found"}]
			return return_response(json.dumps(error, indent=4, sort_keys=False))
	else:

		tourisms = Tourism.publics.filter(tourist=tourist).order_by('-date')
		tourisms = [tourism.get_tourism_json() for tourism in tourisms]
		return return_response(json.dumps(tourisms), indent=4, sort_keys=False)


def api_get_tourisms(request):
	tourisms = Tourism.publics.all().order_by('-date')
	tourisms = [tourism.get_tourism_json() for tourism in tourisms]
	return return_response(json.dumps(tourisms, indent=4, sort_keys=False))


def api_get_single_tourism(request, tourism):
	try:
		tourism = Tourism.publics.get(pk=tourism)
		return return_response(json.dumps(tourism, indent=4, sort_keys=False))
	except Tourism.DoesNotExist:
		error = [{"404":"Tourism Not Found"}]
		return return_response(json.dumps(error, indent=4, sort_keys=False))