# -*- coding: utf-8 -*-
"""
Database models for customerdataapi.
"""

from __future__ import absolute_import, unicode_literals

import collections
import uuid
import jsonfield

from django.db import models


class ApiData(models.Model):
    """
    A simple model to store our customer data
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # pylint: disable=invalid-name
    #data = jsonfield.JSONField(blank=True, null=True, load_kwargs={'object_pairs_hook': collections.OrderedDict})
    ticker=models.CharField(max_length=100)

    price=models.CharField(max_length=100,null=True,blank=True)
    change=models.CharField(max_length=100,null=True,blank=True)
    change_perc=models.CharField(max_length=100,null=True,blank=True)
    market_cap=models.CharField(max_length=100,null=True,blank=True)
    volume=models.CharField(max_length=100,null=True,blank=True)

    last_update=models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return "Data with id <{}>/<{}>".format(self.id,self.ticker)


    @staticmethod
    def crearobjecto(dic_obj):
        keys={'ticker':'ticker',u'l84':'price' , u'p43': 'change_perc', u'c63': 'change', u'j10': 'market_cap', u'v53': 'volume'}
        dic={}
        for key,value in keys.iteritems():
            dic.update({value:dic_obj.get(key,None)})
        print (dic)
        return ApiData(**dic)




