# -*- coding: utf-8 -*-
"""
Views for customerdataapi.
"""
from __future__ import absolute_import, unicode_literals

from rest_framework import viewsets, permissions,generics

from customerdataapi.models import ApiData
from customerdataapi.serializers import  ApiDataSerializer


class ApiDataViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving CustomerData.
    """

    queryset = ApiData.objects.all()
    serializer_class = ApiDataSerializer
    permission_classes = (permissions.AllowAny,)



class ApiDataList(generics.ListAPIView):
    serializer_class = ApiDataSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        ticker= self.kwargs['ticker']
        return ApiData.objects.filter(ticker=ticker)