from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_items(request):
    items = ["Item 1", "Item 2", "Item 3"]
    return Response({"items": items})
