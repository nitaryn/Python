class Human:
	def eat(self):
		print("eating food")

	def talk(self):
		print("Likes talking while eating")

def main():
	frank= Human()
	print(frank)
	frank.eat()
	frank.talk()

if __name__ == '__main__':
	main()
