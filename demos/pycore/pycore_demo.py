
'''
Prereqs:
+ pip install pycorenlp

'''

from pycorenlp import StanfordCoreNLP

import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

import urllib2 as url2
import zipfile
import os
import subprocess
import time


def download_file(url):
	# Open the url
	try:
		f = url2.urlopen(url)
		print "downloading " + url

		with open(os.path.basename(url), "wb") as local_file:
			local_file.write(f.read())

	except url2.HTTPError, e:
		print "HTTP Error:", e.code, url
	except url2.URLError, e:
		print "URL Error:", e.reason, url

def unzip_file(path):
	path_noext = os.path.splitext(path)[0]
	zip_ref = zipfile.ZipFile(path, 'r')
	zip_ref.extractall()
	zip_ref.close()

def open_pycore_server():
	if os.path.exists('./stanford-corenlp-full-2016-10-31.zip'): #isfile
		print 'Archive Present'
	else:
		download_file('http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip')
	

	if os.path.exists('./stanford-corenlp-full-2016-10-31'): #isdir
		print 'Archive unarchived'
	else:
		unzip_file('stanford-corenlp-full-2016-10-31.zip')


	#subprocess.call('run_stanford_corenlp_server.bat', os.P_NOWAIT, shell=True)
	#os.spawnl(os.P_DETACH, '...')
	p = subprocess.Popen('run_stanford_corenlp_server.bat', creationflags=subprocess.CREATE_NEW_CONSOLE) 
	time.sleep(4) # find workaround - ~4s for win 8.1, core i5


def corenlp_tokenize(text):
	nlp = StanfordCoreNLP('http://localhost:9000')
	output = nlp.annotate(text, properties={
		'annotators': 'tokenize,ssplit,pos,depparse,parse',
		'outputFormat': 'json'
	})
	print(output['sentences'][0]['parse'])

	return output



if __name__ == '__main__':
	
	open_pycore_server()

	file_text = open("../source.txt", 'r').read()

	#print 'original: ', file_text
	tokens = corenlp_tokenize(file_text)
	print 'tokenized: ', tokens
	