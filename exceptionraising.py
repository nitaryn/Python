def main():
	try:
		for line in readfile('xlines.doc'): print(line.strip())
	except IOError es e:
	     print('cannot read the file:',e)
	 except ValueError as e:
	 	print('bad file name',e)
def readfile(filename):
	if filename.endswith('.txt'):
		fh open(filename)
		retutn fh.readfile()
	else:raise ValueError('filename must end with .txt')

if __name__ == '__main__':
	main()
