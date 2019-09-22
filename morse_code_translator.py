# Python program to implement Morse Code Translator 

''' 
VARIABLE KEY 
'cipher' -> 'stores the morse translated form of the english string' 
'decipher' -> 'stores the english translated form of the morse string' 
'citext' -> 'stores morse code of a single character' 
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 
'''

# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'} 

# Function to encrypt the string 
# according to the morse code chart 
def encrypt(message): 
	cipher = '' 
	for letter in message: 
		if letter != ' ': 
			cipher += MORSE_CODE_DICT[letter] + ' '
		else: 
			cipher += ' '

	return cipher 

# Function to decrypt the string 
# from morse to english 
def decrypt(message): 

	# extra space added at the end to access the 
	# last morse code 
	message += ' '

	decipher = '' 
	citext = '' 
	for letter in message: 
		if (letter != ' '): 
			i = 0
			citext += letter 
		else: 
			i += 1
			if i == 2 : 
				decipher += ' '
			else: 
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
				.values()).index(citext)] 
				citext = '' 

	return decipher 

def main(): 
	message = "HI,how are you"
	result = encrypt(message.upper()) 
	print (result) 

	message = "--. . . -.- ... -....- ..-.-. . . -.- ... "
	result = decrypt(message) 
	print (result) 
if __name__ == '__main__': 
	main() 
