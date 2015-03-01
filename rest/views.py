from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_response(request) :
	if request.method == 'GET' :
		post_response = {"errorCode":200, "message":"success to get"}
		return JsonResponse(post_response)
	return JsonResponse({"errorCode":404, "message":"not get method"})



@csrf_exempt
def post_response(request) :
	if request.method == 'POST' :
		post_response = {"errorCode":200, "message":"success to post"}
		return JsonResponse(post_response)
	return JsonResponse({"errorCode":404, "message":"not post method"})


@csrf_exempt
def put_response(request) :
	if request.method == 'PUT' :
		put_response = {"errorCode":200, "message":"success to put"}
		return JsonResponse(put_response)
	return JsonResponse({"errorCode":404, "message":"not put method"})		


@csrf_exempt
def patch_response(request) :
	if request.method == 'PATCH' :
		patch_response = {"errorCode":200, "message":"success to patch"}
		return JsonResponse(patch_response)
	return JsonResponse({"errorCode":404, "message":"not patch method"})			


@csrf_exempt
def delete_response(request) :
	if request.method == 'DELETE' :
		delete_response = {"errorCode":200, "message":"success to delete"}
		return JsonResponse(delete_response)
	return JsonResponse({"errorCode":404, "message":"not delete method"})	
