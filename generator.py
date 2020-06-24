from random import randint
import string
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--size", required=False, type=int, default=16,
                help="password size")
ap.add_argument("-l", "--lower", required=False, action='store_true',
                help="use lowercase letters")
ap.add_argument("-u", "--upper", required=False, action='store_true',
                help="use uppercase letters")
ap.add_argument("-d", "--digits", required=False, action='store_true',
                help="use digits")
ap.add_argument("-p", "--punct", required=False, action='store_true',
                help="use punctuation")
args = ap.parse_args()

characters = ""
password = ""
if args.lower:
    characters += string.ascii_lowercase
if args.upper:
    characters += string.ascii_uppercase
if args.digits:
    characters += string.digits
if args.punct:
    characters += string.punctuation

if characters:
    for i in range(0, args.size):
        password += characters[randint(0, len(characters) - 1)]

    print(password)
