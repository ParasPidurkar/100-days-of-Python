import random
letters=['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['1','2','3','4','5','6','7','8','9','0']
symbols=['+','_','*','&','^','%','$','#','@','!']

noOfChar = int(input("No of char in  your pass"))
noOfSymbols=int(input("No of symbols in  your pass"))
noOfDigits= int(input("No of digits in  your pass"))

password=""

for letter in range(1,noOfChar+1):
    random_char = random.choice(letters);
    password = password + random_char

for letter in range(1,noOfDigits+1):
    random_char = random.choice(number);
    password = password + random_char

for letter in range(1,noOfSymbols+1):
    password += random.choice(symbols);
    #password = password + random_char

print(password)