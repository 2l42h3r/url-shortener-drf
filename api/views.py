from django.shortcuts import redirect
from rest_framework.response import Response
from django.http import HttpResponseBadRequest, Http404
from rest_framework.decorators import api_view
from .models import UrlList
from .serializers import UrlListSerializer

from random import choice
import string

length = 5

def generate_shortened(length: int) -> str:
    return "".join(choice(string.ascii_letters + string.digits) for _ in range(length))

@api_view(['POST'])
def shorten(request):
    url = request.data['url']

    if url is None:
        raise HttpResponseBadRequest

    shortened = generate_shortened(length)

    UrlList.objects.create(
        fullurl=url,
        shortened=shortened
    )

    return Response({'shortened': shortened})

def redirect_url(request, shortened):
    try:
        found_shortened = UrlList.objects.get(shortened=shortened)
    except UrlList.DoesNotExist:
        found_shortened = None

    if found_shortened is None:
        raise Http404

    return redirect(found_shortened.fullurl)
