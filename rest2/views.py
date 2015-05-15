from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class MyView(View):
	

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(MyView, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		return JsonResponse({'message':'success to GET'})

	def post(self, request):
		return JsonResponse({'message':'success to POST'})
		# or with parameter request  
		# return JsonResponse({'object':request.POST.get('param')})
		
	def put(self, request):
		return JsonResponse({'message':'success to PUT'})
		
	def patch(self, request):
		return JsonResponse({'message':'success to PATCH'})
	
	def delete(self, request):
		return JsonResponse({'message':'success to DELETE'})			