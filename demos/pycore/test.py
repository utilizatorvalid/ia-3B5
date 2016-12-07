import unittest
import pycore_demo
from sys import flags
from sys import argv

# 'and' operator shortcircuits by default if first condition fails
# if first condition succeeds, second operand won't have index out of range
if len(argv) > 1 and argv[1] == '-v':
	verbose = True
else:
	verbose = flags.verbose

class MyTest(unittest.TestCase):
	def setUp(self):
		pycore_demo.open_pycore_server()
	def test_tokenize(self):
		if not verbose:
			print '\n --- Testing function corenlp_tokenize() ----'
		#self.assertEqual(pycore_demo.corenlp_tokenize('Hello, my name is'), ['Hello', ',', 'my', 'name', 'is'])
			#doesn't take into account annotators
	
if __name__ == '__main__':
	unittest.main()