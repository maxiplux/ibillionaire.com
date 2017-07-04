import re
import json

import requests

from django.core.management.base import BaseCommand
from django.conf import  settings
from customerdataapi.models import ApiData
from django.utils import timezone


class Command(BaseCommand):
	help = 'Pruebas'

	def parse_line(self, line):
		# ayuda tomada de https://www.reddit.com/r/learnpython/comments/1wlxj7/asyncioaiohttp_yahoo_finance_streamerapi_webclient/, https://github.com/ezl/yahoofinance/blob/master/liveticker.py
		if 'yfs_u1f' in line:
			try:
				line = re.match(r".*?\((.*?)\)", line)
				line = line.group(1)
				line = re.sub(r"(\w\d\d):", '"\\1":', line)
				return json.loads(line), True
			except:
				return {}, False
		if 'yfs_mktmcb' in line:
			line = re.match(r".*?\((.*?)\)", line)
			line = line.group(1)
			return json.loads(line), True
		return {}, False


	def handle(self, *args, **options):  # ApiData
		response = requests.get(settings.URL_STREAM, stream=True)
		for chunk in response.iter_content(chunk_size=512):
			if chunk:  # filter out keep-alive new chunks
				obj,status=self.parse_line(chunk)
				if status and 'TSLA' in obj.keys():
					# asumiendo que solamente estamos consultando TSLA , SEGUN COREO DE CONSULTA ,
					obj=obj.get('TSLA',None)
					if obj:
						obj.update({'ticker':'TSLA'})
						obj.update({'last_update':timezone.now()})
						api=ApiData.crearobjecto(obj)
						api.save()
						print (api.id)
				else:
					print ("Esperando Datos"+str(obj))