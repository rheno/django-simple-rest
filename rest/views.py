from django.shortcuts import render
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_response(request) :
	if request.method == 'GET' :
 		msg = request.GET.get('message')
		post_response = {"errorCode" : 200, "message" : msg}
		return JsonResponse(post_response)
	return JsonResponse({"errorCode":404, "message":"not get method"})



@csrf_exempt
def post_response(request) :
	if request.method == 'POST' :
                post = QueryDict(request.body)
                msg = post.get('message')
		post_response = {"errorCode" : 200, "message" : msg}
		return JsonResponse(post_response)
	return JsonResponse({"errorCode" : 404, "message" : "not post method"})


@csrf_exempt
def put_response(request) :
	if request.method == 'PUT' :
		put = QueryDict(request.body)
   		msg = put.get('message')
		put_response = {"errorCode" : 200, "message" : msg}
		return JsonResponse(put_response)
	return JsonResponse({"errorCode" : 404, "message" : "not put method"})		


@csrf_exempt
def patch_response(request) :
	if request.method == 'PATCH' :
		patch = QueryDict(request.body)
 		msg = patch.get('message')
		patch_response = {"errorCode" : 200, "message" : msg}
		return JsonResponse(patch_response)
	return JsonResponse({"errorCode" : 404, "message" : "not patch method"})			


@csrf_exempt
def delete_response(request) :
	if request.method == 'DELETE' :
		delete = QueryDict(request.body)
 		msg = delete.get('message')
		delete_response = {"errorCode" : 200, "message" : msg}
		return JsonResponse(delete_response)
	return JsonResponse({"errorCode":404, "message":"not delete method"})	
