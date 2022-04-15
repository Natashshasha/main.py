import os
import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse')
parser.add_argument('-n', '--name', nargs='?', default='Anonymous', help="Here's your name")
parser.add_argument('-p', '--path', help="Here's the path to your file")
parser.add_argument('-nQ', '--noQ', action="store_true", help="No more questions, mate")
args = parser.parse_args()
print(f'Hi {args.name}!')
print(os.getcwd())
print(args)
if os.path.exists(args.path):
    if args.noQ:
        os.remove(args.path)
        exit(0)
    else:
        ag = input(f'\n{args.name}, Вы действительно хотите удалить этот файл?').capitalize()
        if ag[0] == 'Y':
            os.remove(args.path)
        else:
            print('Very well, I do nothing')
else:
    print("\nSorry, mate, but your file doesn't exist :P")