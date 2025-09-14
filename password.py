print("------PASSWORD GENERATOR------")

length = int(input("Enter the desired password length: "))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@#$%&*_+=,./:;<>^-"
all_char = letters + digits + special

password = ""
for i in range(length):
    p = (i*37 + length *11) % len(all_char)
    password += all_char[p]

print("Generated password:",password)