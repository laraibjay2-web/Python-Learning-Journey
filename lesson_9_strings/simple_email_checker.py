user_email = input("Enter your email: ").strip().lower()
print("Cleaned email:", user_email)
print("contains @:", user_email.find("@") != -1)
print("ends with .com:", user_email.endswith(".com"))
