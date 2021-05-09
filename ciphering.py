# Alphabet with 26 letters
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("Welcome to The Cipher_Machine!")

walrus_input= input("Would you like to encode or decode your message?: ")

string_input = input("Enter your message: ")

key = int(input("Enter your key: "))

n = len(string_input)

string_output= ""

for i in range(n):
    character = string_input[i]
    location = alphabet.find(character)
                             
    if (walrus_input == "decode"):
         new_location= (location - key) % 26
         string_output += alphabet[new_location]
        
    elif (walrus_input == "encode"):
        new_location= (location + key) % 26
        string_output += alphabet[new_location]
    else:
        print("error")
        
        
print("All done: ", string_output)
print("Thanks for using our Cipher_Machine!")

