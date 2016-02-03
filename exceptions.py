try:
	fh= open('xlines.txt')
	for line in fh,readlines():
		print(line)
except:
	print("something wrong happened")
	print("after badness")
