import os
import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse')
parser.add_argument('-n', '--name', nargs='?', default='Некто', help="Это твое имя")
parser.add_argument('-p', '--path', help="Это путь к твоему файлу")
parser.add_argument('-nQ', '--noQ', action="store_true", help="Больше нет вопросов")
args = parser.parse_args()
print(f'Hi {args.name}!')
print(args)

if os.path.exists(args.path):
    if args.noQ:
        os.remove(args.path)
        exit(0)
    else:
        ag = input(f'\n{args.name}, Ты действительно хочешь удалить этот файл? ').capitalize()
        if ag[0] == 'Д':
            os.remove(args.path)
        else:
            print('Хорошо, ничего не буду делать)')
else:
    print("\nПрости, но я не смог найти этот файл(")