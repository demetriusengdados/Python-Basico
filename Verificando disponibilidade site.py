import urllib 
import urllib.request


try:
  site = urllib.request.urlopen('http://www.facebook.com.br')
except urllib.error.URLError:
  print('Não consegui conectar')
else:
  print('Consegui conectar')
  