from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from quote_app.models import Quote, QuoteCategory
from quote_app.serializers import QuoteCategorySerializer, QuoteSerialaizerList, QuoteSerialaizer

# Create your views here.

"""Quote Category"""
@api_view(['GET'])
def get_categories(request: Request) -> Response:
    quotes_categories = QuoteCategory.objects.all().order_by('id')
    serializer = QuoteCategorySerializer(instance=quotes_categories, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_category(request: Request, pk: int) -> Response:
    try:
        quotes_category = QuoteCategory.objects.get(id=pk)
    except QuoteCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = QuoteCategorySerializer(instance=quotes_category)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_category(request: Request) -> Response:
    serializer = QuoteCategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_category(request: Request, pk: int) -> Response:
    try:
        quotes_category = QuoteCategory.objects.get(id=pk)
    except QuoteCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = QuoteCategorySerializer(instance=quotes_category, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_category(request: Request, pk: int) -> Response:
    try:
        quotes_category = QuoteCategory.objects.get(id=pk)
    except QuoteCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    quotes_category.delete()

    return Response('category successfully deleted!')

"""Quote"""
@api_view(['GET'])
def get_quotes(request: Request) -> Response:
    quotes = Quote.objects.all().order_by('id')
    serializer = QuoteSerialaizerList(instance=quotes, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_quote(request: Request, pk: int) -> Response:
    try:
        quote = Quote.objects.get(id=pk)
    except Quote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = QuoteSerialaizerList(instance=quote)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_quote(request: Request) -> Response:
    serializer = QuoteSerialaizer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_quote(request: Request, pk: int) -> Response:
    try:
        quote = Quote.objects.get(id=pk)
    except Quote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = QuoteSerialaizer(instance=quote, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_quote(request: Request, pk: int) -> Response:
    try:
        quote = Quote.objects.get(id=pk)
    except Quote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    quote.delete()

    return Response('quote successfully deleted!')