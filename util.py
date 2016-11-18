import re
class Util:
	name = "testName"
	def pl(self, s):
		print(s)
		return

def p(s):
	print(s)

def extract(route):
	pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", re.I)
	match = pattern.search(route)
	return match.group()

def test(**args):
	print(args['arg'])
	return

file = open("test.txt", "w+")
string = "abc".encode('utf-8') + "\n"
file.write(string)
file.close()