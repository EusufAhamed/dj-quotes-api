from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request: Request) -> Response:
    data = {
        'message': 'quote app',
        'method': request.method
    }
    return Response(data={'message': data}, status=status.HTTP_200_OK)