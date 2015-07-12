from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class MyView(View):
	

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(MyView, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		msg = request.GET.get('message')	
		return JsonResponse({'message' : msg})

	def post(self, request):
		post = QueryDict(request.body)
		msg = post.get('message')
		return JsonResponse({'message' : msg})
		# or with parameter request  
		# return JsonResponse({'object':request.POST.get('param')})
		
	def put(self, request):
		put = QueryDict(request.body)
		msg = put.get('message')
		return JsonResponse({'message' : msg})
		
	def patch(self, request):
		patch = QueryDict(request.body)
		msg = patch.get('message')
		return JsonResponse({'message' : msg})
	
	def delete(self, request):
		delete = QueryDict(request.body)
		msg = delete.get('message')
		return JsonResponse({'message' : msg})			
