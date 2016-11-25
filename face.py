import requests
import json
class user:
	
	def __init__(self):
		self.url = "https://graph.facebook.com/v2.8/me"
		self.token = "EAACEdEose0cBADZCODjQZBGZCvVZAROlm1tfTNT3U5Se1ZCfwq3U2zSJ0XXWf717HB2WoI51s33XqSiT1WSjfPKhUN1LnG9JMKdlUm1hAL7Wca2LujoLPvLPusX6tER1qPdbZA1KCfF5hv7Haby9fbGDjB6EsuGJqW0wFqbMnYQwZDZD"
	

	def obtenerinformacion(self):
		parametros = {"access_token": self.token}
		resultado = requests.get(self.url, params=parametros).json()
		print(resultado)
		self.nombre = resultado["name"]
		return resultado

	def publicarComentario(self, message):
		self.url = "https://graph.facebook.com/v2.8/feed" 
		parametros = {"message": message, "access_token": self.token} 
		resultado = requests.post(self.url, params=parametros).json()
		print(resultado)
		return resultado

