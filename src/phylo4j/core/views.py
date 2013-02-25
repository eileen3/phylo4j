from django.http import HttpRequest, HttpResponse
from phylo4j.core.models import Enzyme


def home(request):
	enzyme = Enzyme.index.get(enzyme_id_index = '1.1.1.7')
	return HttpResponse(enzyme.official_name)
