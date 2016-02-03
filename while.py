def main():
	a, b = 10, 80
	while b<100:
		print (b, end = '')
		a,b = b, a+b

if __name__ == '__main__':
	main()
