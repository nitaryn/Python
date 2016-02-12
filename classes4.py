class Mammal:
	def talk(self):print('I am a cold blooded mammal!')
	def think(self):print('I have the highest thinking capacity')
	def scale(self):print('I do not have scales')


class Human(Mammal):
	def eat(self):
		print("eating food")

	def talk(self):
		super().talk()
		print("Talks while eating")

def main():
	frank= Human()
	frank.eat()
	frank.talk()


if __name__ == '__main__':
	main()
