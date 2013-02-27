from django.http import HttpRequest, HttpResponse
from phylo4j.util.request import render_page
from phylo4j.core.models import Enzyme


def index(request):
	enzyme = Enzyme.index.get(enzyme_id_index = '1.1.1.7')
	return render_page(request, 'index', { 'name' : enzyme.official_name })
