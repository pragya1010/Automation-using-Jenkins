def palindrome(s):
	if isinstance(s, str):
		return s[::-1] 
	else:
		s = str(s)
		return int(s[::-1])