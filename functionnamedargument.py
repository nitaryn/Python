def main():
	testfunc(9,1,3,6,0,1,two=2,four=55,seven=34)

def testfunc (num,int,string,*args,**kwargs):
	print('This is my test function',kwargs['two'],kwargs['four'],kwargs['seven'])

if __name__ == '__main__':
	main()
