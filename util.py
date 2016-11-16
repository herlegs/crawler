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

list = ['Route:52.198.61.109/32','Route:52.199.48.176/32','Route:10.200.26.0/24']
converted = [extract(x) for x in list]
print(converted)