class Human:
	def__init__ (self, **kwargs):
		self.properties =  kwargs

    def eat(self):
		print("eating food")

	def talk(self):
		print("Talks while eating")

	def get_properties(self):
	    return self.properties

	def get_properties(self, key):
		return self.properties.get(key, None)


	    @property
	    def sex(self):
	    	return self.properties.get('sex',None)

	    @sex.setter
	    def sex(self,s):
	    	self.properties['color'] = s

	    @sex.deleter
	    def sex(self):
	    	del self.properties['sex']

def main():
	    frank= Human(sex='male')
	    frank.sex = 'male'
	    print(frank.sex)

if __name__ == '__main__':
	main()
