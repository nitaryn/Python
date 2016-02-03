class Mango:
	def _init_(self, kind = "ripe"):
		self.ripe = kind

	def whatkind (self):
		return self.kind

def main():
	raw = Mango()
	eatable = Mango("eatable")
	print (eatable.whatkind())

if __name__ == '__main__':main()

