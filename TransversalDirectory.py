paths_wordpress = {'wp-login.php':
	['index.php','license.txt','readme.html',
	'wp-activate.php', 'wp-app.php',
	'wp-blog-header.php', 'wp-comments-post.php',
	'wp-config-sample.php', 'wp-cron.php',
	'wp-links-opml.php', 'wp-load.php',
	'wp-mail.php',
	'wp-pass.php', 'wp-register.php',
	'wp-settings.php', 'wp-signup.php',
	'wp-trackback.php', 'xmlrpc.php']
}

paths_recursos = [
	'includes','js',
	'css', 'src',
	'img', 'includ',
	'../../../../../',
	'docs', 'pdfs',
	'pdf', 'documents',
	'fotos', 'photos',
]

body_files = {}

import os
import urllib
import sys
from bs4 import BeautifulSoup

continuando = False
for urlsWP, files in paths_wordpress.items():
	response = urllib.urlopen(sys.argv[1]+'/'+urlsWP)
	if response.getcode()==int(200) and continuando==False:
		print "CMS WORDPRESS ENCONTRADO"
		for f in files:
			response = urllib.urlopen(sys.argv[1]+'/'+urlsWP)
			if response.getcode()==int(200):
				print "PATHS ENCONTRADOS"
				print response.geturl()
	else:
		print "WORDPRESS NO ENCONTRADO"

for path in paths_recursos:
	response = urllib.urlopen(sys.argv[1]+'/'+path+'/')
	if response.getcode()==200:
		print "PATHS ENCONTRADOS"
		html_tags = BeautifulSoup(response,"lxml")
		file_html=html_tags.find_all('a')
		arrays = []
		for f_h in file_html:
			arrays.append(f_h.get('href'))
		body_files[path] = arrays
		print response.geturl()

if len(body_files):
	while True:
		print body_files.keys()
		key_paths = raw_input('Ingrese el path que desea mostrar: ')
		try:
			print body_files[key_paths]
		except Exception, e:
			print "valor ingresado incorrecto"
		finally:
			yes_no = raw_input('Desea Salir? Y/N :')
			if yes_no!='n' or str.upper(yes_no) != 'N':
				break

contenido = urllib.urlopen(sys.argv[1]+'/robots.txt').read()
if contenido.getcode()==200:
	print contenido
