import unittest
import nltk_demo
from sys import flags
from sys import argv

# 'and' operator shortcircuits by default if first condition fails
# if first condition succeeds, second operand won't have index out of range
if len(argv) > 1 and argv[1] == '-v':
	verbose = True
else:
	verbose = flags.verbose

class MyTest(unittest.TestCase):
	def test_lemmatize(self):
		if not verbose:
			print '\n --- Testing function nltk_lemmatize() ----'
		self.assertEqual(nltk_demo.nltk_lemmatize(['Hello', ',', 'my', 'name', 'is']), ['Hello', ',', 'my', 'name', 'is'])

	def test_tokenize(self):
		if not verbose:
			print '\n --- Testing function nltk_tokenize() ----'
		self.assertEqual(nltk_demo.nltk_tokenize('Hello, my name is'), ['Hello', ',', 'my', 'name', 'is'])

if __name__ == '__main__':
	unittest.main()