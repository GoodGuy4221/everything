import sys
import argparse


def show_user(name, *args):
    message = [f'name user {name}']
    if args:
        message.append(f'age {args[0]}')
    print(', '.join(message))


# print(sys.argv)
# app, *args = sys.argv
# print(app, *args, sep='\n')

args = sys.argv[1:]
# print(args)
if args:
    show_user(*args)
else:
    name = input('enter name ')
    show_user(name)
