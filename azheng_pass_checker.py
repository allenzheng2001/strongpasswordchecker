iterations = 0 #global variable

def checkUp(character):
	return (ord(character) <= 90 and ord(character) >= 65)

def checkLow(character):
	return (ord(character) <= 122 and ord(character) >= 97)

def checkNum(character):
	return (ord(character) <= 57 and ord(character) >=48)

def checkSym(character):
	return ( 
			(ord(character) >= 33 and ord(character) <=47) or
			(ord(character) >= 91 and ord(character) <=96) or
			(ord(character) >= 123 and ord(character) <=126))


def main():
	global iterations # global variable

	if (iterations == 0):
		password = input("A strong password contains all of the following: \n \t-both an uppercase and lowercase letter \n \t-a number \n \t-a symbol \n \t-between 8-16 characters. \n \n Please enter a password:")
	else:
		password = input("Please try again. Enter a new password:")
	hasUp = False
	hasLow = False	
	hasNum = False
	hasSym = False
	length = 0

	for character in password:
		if checkUp(character):
			hasUp = True
		if checkLow(character):
			hasLow = True	
		if checkNum(character):
			hasNum = True
		if checkSym(character):
			hasSym = True
		length += 1

	# 1 uppercase and 1 lowercase, 1 number, 1 special character, 8-16 characters

	if (hasUp and hasLow and hasNum and hasSym and length >= 8 and length <= 16):
		print("\nYour password is strong.")

	else :
		print("\nYour password is too weak, please consider:")
		if (not hasUp):
			print ("-including an uppercase letter")
		if (not hasLow):
			print ("-including a lowercase letter")
		if (not hasNum):
			print ("-including a number")
		if (not hasSym):
			print ("-including a symbol")
		if (not (length >= 8 and length <= 16)):
			print ("-changing its length to between 8 to 16 characters")
		print()
		iterations+=1
		main()			

main()



# 