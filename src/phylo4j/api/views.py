from neomodel.exception import DoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONRenderer, JSONPRenderer
from rest_framework.response import Response
from serializers import ProteinSerializer

from phylo4j.bio4j.models import Protein

#root api entry point
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
    })


class ProteinDetail(APIView):

    renderer_classes = (JSONRenderer, JSONPRenderer)

    def get(self, request, format=None, **kwargs):
        try:
            protein = Protein.index.get(protein_accession_index=kwargs['accession'])
            serializer = ProteinSerializer(protein)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DoesNotExist:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

