
'''
Prereqs:
+ pip install pycorenlp


'''

from pycorenlp import StanfordCoreNLP

import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

import urllib2
import zipfile
import os

file_text = open("source.txt", 'r').read()


def download_file(url):
    # Open the url
    try:
        f = urlopen(url)
        print "downloading " + url

        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(f.read())

    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url

def unzip_file(path):	
	zip_ref = zipfile.ZipFile(path, 'r')
	zip_ref.extractall(os.path.basename(path))
	zip_ref.close()

#download_file('http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip')
#unzip_file('stanford-corenlp-full-2016-10-31.zip')


#subprocess.call('run_stanford_corenlp_server.bat', os.P_NOWAIT, shell=True)
#os.spawnl(os.P_DETACH, 'some_long_running_command')

def corenlp_tokenize(text):
    nlp = StanfordCoreNLP('http://localhost:9000')
    output = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    print(output['sentences'][0]['parse'])

    return output


print 'original: ', file_text
tokens = corenlp_tokenize(file_text)
print 'tokenized: ', tokens
