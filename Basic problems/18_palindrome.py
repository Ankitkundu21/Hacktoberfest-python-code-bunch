n = input()
b = list(n)
b_rev = b[::-1]
if(b == b_rev):
	print('It is a Plaindrome')
else:
	print('It is not a Palindrome')
