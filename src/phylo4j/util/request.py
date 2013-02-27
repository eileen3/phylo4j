from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def render_page(request, template_name, dictionary={}, context_instance=None, mimetype=None):
	assert isinstance(request, HttpRequest)
	template_name += '.djhtml'
	context_instance = context_instance or RequestContext(request)
	return render_to_response(template_name, dictionary, context_instance=context_instance, mimetype=mimetype)
