def main():
	try:
	    fh = open('xlines.txt')
	    for line in fh: print (line.strip())
	expept IOError as e:
	     print('adjust the error:',e)

if __name__ == '__main__':
	main()

