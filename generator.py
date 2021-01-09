#!/usr/bin/env python3

from random import randint
from argparse import ArgumentParser
import string

parser = ArgumentParser()
parser.add_argument("-s", "--size", required=False, type=int, default=16,
                    help="password size")
parser.add_argument("-l", "--lower", required=False, action='store_true',
                    help="use lowercase letters")
parser.add_argument("-u", "--upper", required=False, action='store_true',
                    help="use uppercase letters")
parser.add_argument("-d", "--digits", required=False, action='store_true',
                    help="use digits")
parser.add_argument("-p", "--punct", required=False, action='store_true',
                    help="use punctuation")
args = parser.parse_args()

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
    for x in range(args.size):
        password += characters[randint(0, len(characters) - 1)]

    print(password)
