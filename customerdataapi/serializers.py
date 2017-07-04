# -*- coding: utf-8 -*-
"""
Database models for customerdataapi.
"""

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from customerdataapi.models import ApiData


class ApiDataSerializer(serializers.ModelSerializer):
    """
    A simple serializer for our CustomerData model
    """
    id = serializers.ReadOnlyField()  # pylint: disable=invalid-name
    #data = serializers.JSONField()
    class Meta:
        model = ApiData
        fields = ('id', 'ticker','price','change','change_perc','market_cap','volume','last_update')
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """

        instance.data = validated_data.get('data', instance.data)
        instance.save()
        return instance