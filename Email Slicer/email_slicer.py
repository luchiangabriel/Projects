
print("Welcome to The Email Slicer\n")

email = input("Please enter your email here: ").strip()

username = email[:email.index("@")]

domain = email[email.index("@") + 1:]

display = "\nYour username is '{}' and your domain name is '{}'.".format(username, domain)

print(display)
