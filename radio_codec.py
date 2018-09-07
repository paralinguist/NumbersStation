encoding = ['', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'ESCAPE', 'RUN', '!', 'PEOPLE', '.', ',', '(', ')', '+', '"', ':', '?', '-']
number_words = "zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty-one","twenty-two","twenty-three","twenty-four","twenty-five","twenty-six","twenty-seven","twenty-eight","twenty-nine","thirty","thirty-one","thirty-two","thirty-three","thirty-four","thirty-five","thirty-six","thirty-seven","thirty-eight","thirty-nine","fourty"

def decode_character(encoded_num):
  return encoding[encoded_num]                     

def encode_character(letter):
  return encoding.index(letter)

def encryptcharacter(letter,keynumber):
  number = encode_character(letter)
  keynumber = keynumber+number
  if keynumber >40:
    keynumber = keynumber-40
  return keynumber

def decryptcharacter(number,keynumber):
  number = number-keynumber
  if number < 0:
      number = number - 1
  letter = decode_character(number)
  return letter

def encrypt_string(plaintext, key):
  keypos = 0
  cyphertext = ''
  for letter in plaintext:
    keynumber = int(key[keypos])
    cyphernumber = encryptcharacter(letter,keynumber)
    keypos = keypos+1
    cyphertext = cyphertext+' '+str(cyphernumber)
  return cyphertext

def decrypt_string(cipher, key):
  letters = ""
  numbers = cipher.split(" ")
  key = key.split(' ')
  i = 0
  for number in numbers:
    letters = letters+decryptcharacter(int(number), int(key[i]))
    i = i + 1
  return letters

def convert_to_words(numbers_in):
  numbers_as_words = []
  for number in numbers_in:
    if int(number) < 10:
        numbers_as_words.append('zero')
    numbers_as_words = numbers_as_words + number_words[int(number)].split('-')
  return numbers_as_words
  #os.system("aplay ../Numbers/"+ b +".wav")
