import random

from phylo4j.util.request import render_page
from phylo4j.bio4j.models import Enzyme


def index(request):
    # enzyme_index = '1.1.1.' + str(random.randint(0, 300))
    # enzyme = Enzyme.index.get(enzyme_id_index = enzyme_index)
    return render_page(request, 'index', {'name': 'something',
                                'catalytic_activity': 'something',
                                'comment': 'something'})
