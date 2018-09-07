import io
from subprocess import check_output
import radio_codec
from time import sleep
from random import randint
keys = []
def broadcast(number):
    #check_output(['./pifm','/home/jonathan/numbers_wav/'+number+'.wav','103.3','22050','stereo'])
    check_output(['aplay','/home/jonathan/numbers_wav/'+number+'.wav'])

def get_key(pairs_needed):
    key = []
    pairs_per_line = 13
    lines = 25
    max_line = lines - int(pairs_needed / pairs_per_line)
    start_line = randint(0, max_line-1)
    end_line = start_line + int(pairs_needed / pairs_per_line)
    with open('otp.txt') as otp:
        for i, line in enumerate(otp):
            if (i) >= start_line and (i) <= end_line:
                key = key + line.rstrip().split(' ')
    return start_line+1, key

def transmit_message(message):
    start_line, key = get_key(len(message))
    print('Start: ' + str(start_line))
    start_line_word = radio_codec.number_words[start_line].split('-')
    for i in range(3):
        broadcast('zero')
    sleep(1)
    for i in range(3):
        for word in start_line_word:
            broadcast(word)
    sleep(1)
    for i in range(3):
        broadcast('nine')
    sleep(3)
    numbers = radio_codec.encrypt_string(message, key)
    numbers = numbers.strip().split(' ')
    numbers_as_words = radio_codec.convert_to_words(numbers)
    i = 0
    while i < len(numbers_as_words):
        first_digit = numbers_as_words[i]
        number = radio_codec.number_words.index(first_digit)
        broadcast(first_digit)
        print(number)
        second_number = 0
        if i + 1 < len(numbers_as_words):
            second_digit = numbers_as_words[i + 1]
            second_number = radio_codec.number_words.index(second_digit)
        if number < 10 or (number in [20,30,40] and (second_number > 0 and second_number < 10)):
            second_digit = numbers_as_words[i + 1]
            broadcast(second_digit)
            print(second_number)
            i = i + 1
        i = i + 1
        print('---')
        sleep(1)
while True:
    #message one
    broadcast('butterflying')
    transmit_message('HELLO WORLD')
    #message two
    broadcast('hector_steps_out')
    transmit_message('ASC STEM ROCKS!')
    #message three
    broadcast('tetris_theme')
    transmit_message('DO YOU DO CRYPTO?')
