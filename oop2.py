class AnimalAction:
	"""docstring for AnimalAction"""
	def quack(self):return self.strings['quack']
	def feathers(self):return self.strings['feathers']
	def bark(self):return self.strings['bark']
	def fur(self):return self.strings['fur']
class Duck(AnimalAction):
	strings = dict(
		quack ="quaaaaaak!",
		feathers ="The duck has grey and white feathers.",
		bark ="The duck cannot bark",
		fur ="The duck has no fur",
	)
class person(AnimalAction):
	strings = dict(
		quack ="The person imitates the duck",
		feathers ="The person takes the feathers from the ground and shows it.",
		bark ="The person says woof!",
		fur ="The puts on a fur coat",

	)

class Dog(AnimalAction):
	strings = dict(
		quack ="The dog cannot quack",
		feathers ="The dog has no feathers .",
		bark ="Arf!",
		fur ="The dog has white fur with black spots.",

	)
def in_the_doghouse (dog):
	print(dog.burk())
	print(dog.fur())

def in_the_forest(duck):
	print(duck.quack())
	print(duck.feathers())

def main():
	donald = Duck()
	john = person()
	fido = Dog()

	print("In the forest")
	for o in (donald, john,fido):
		in_the_forest(o)

	print("in_the_doghouse")
	for o in(donald,john,fido):
		in_the_doghouse(o)

if __name__ == '__main__': main()









