#! /usr/bin/env python
from bf import bf
import argparse

parser = argparse.ArgumentParser(description="Command-Line bf runner")

# parser.add_argument()

parser.add_argument("-c", "--code", help = "code to parse")
parser.add_argument("-i", "--input", help = "input to use")

args = parser.parse_args()

if (args.input == None or args.code == None):
  print("Must provide code and input")

interpreter = bf(args.code, args.input)

print(interpreter.run())