# -*- coding: utf-8 -*-
"""
Admin views to update the models using the built in admin funciont
"""
from __future__ import unicode_literals

from django.contrib import admin

from customerdataapi.models import ApiData


admin.site.register(ApiData)
