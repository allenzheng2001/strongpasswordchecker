# if __name__ ==  "__main__":
def main():
	check_password()

def check_password():
	password = input("Choose new password: ")

	pass_len = len(password)
	length_req = len(password) >= 8 and len(password) <= 16

	special_chars = ["!@#$"]

	has_upper = False
	has_lower = False
	has_numeric = False
	has_symbol = False

	for char in password:
		if char.isupper():
			has_upper = True
		elif char.islower():
			has_lower = True
		elif char.isnumeric():
			has_numeric = True
		elif char in special_chars:
			has_symbol = True

	strong_pass = has_upper and has_lower and has_numeric and has_symbol and length_req

	if strong_pass:
		print("Your password is strong.")
	else:
		print("Your password is weak. You need:")
		if not has_upper:
			print("an uppercase letter")
		if not has_lower:
			print("a lowercase letter")
		if not has_numeric:
			print("a number")
		if not has_symbol:
			print("a symbol")
		if not length_req:
			print("a password length between 8 and 16 characters")
		check_password()

main()
