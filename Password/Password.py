passwordFile = open("SecretPasswordFile.txt")
secretPassword = passwordFile.read()

print("Enter your password: ")
typedPassword = input()

if typedPassword == secretPassword:
    print("Access Granted")
elif typedPassword == "12345":
    print("That's a silly password!")
else:
    print("Access Denied")