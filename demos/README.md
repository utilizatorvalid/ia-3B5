# ia-3B5
Artificial Intelligence project

## Updates

**Log**:
+ `This section will be updated soon`

Webpage: [2b5.github.io/ia-3B5/](https://2b5.github.io/ia-3B5/)

#### Folder structure:
+ `nltk/` and `pycore/` - implementations - tokenize and lemmatize
  + both have tests, which you can run by: `py -2.7 test_sample.py [-v]` (verbose argument optional)
  + you could also automatically discover tests in a folder: `python -m unittest discover`
  + install code coverage: `pip install coverage` (*`testing`* - or you could install the requirements with: `pip install -r requirements.txt`)
  + to run code coverage: `coverage run test.py`
  + generate report (in console): `coverage report -m`
  + export report (html): `coverage html`
+ `gTTS/` - Google TTS (Text to Speech) wrapper ([docs](https://github.com/pndurette/gTTS))
  + alternative: [alexa-tts-demo](https://github.com/ewenchou/alexa-tts-demo) ([note](https://www.quora.com/Who-is-the-text-to-speech-TTS-vendor-of-Amazon-Echo))
  + can be used in PyQt interface ([example](https://wiki.python.org/moin/PyQt/Playing%20a%20sound%20with%20QtMultimedia))
+ `tests/` - unit tests for the previous two


## Useful Links
+ https://stanfordnlp.github.io/CoreNLP/corenlp-server.html#getting-started  
+ https://stanfordnlp.github.io/CoreNLP/  
+ https://github.com/smilli/py-corenlp  
+ folder structure and other tips & tricks: http://docs.python-guide.org/en/latest/writing/structure/
+ logging - https://docs.python.org/2/howto/logging.html
+ unit testing in python:
  + https://docs.python.org/2/library/unittest.html
  + http://pythontesting.net/framework/unittest/unittest-introduction/
  + http://www.onlamp.com/pub/a/python/2004/12/02/tdd_pyunit.html
  + http://www.diveintopython.net/unit_testing/index.html#roman.intro
  + http://docs.python-guide.org/en/latest/writing/tests/
  + http://www.drdobbs.com/testing/unit-testing-with-python/240165163
  + https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
  + https://stackoverflow.com/questions/1732438/how-to-run-all-python-unit-tests-in-a-directory
+ translate module: [google-api-python-client](https://developers.google.com/api-client-library/python/apis/translate/v2)
+ code coverage module: https://coverage.readthedocs.io/en/latest/
