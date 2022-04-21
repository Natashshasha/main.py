import os
import argparse
import configparser
import pickle

print(os.getcwd())


class Cartoon:
    def __init__(self, name, genre, origin, main_character):
        self.name = name
        self.genre = genre
        self.origin = origin
        self.main_character = main_character

    def __str__(self):
        return f"Cartoon's name: {self.name} \nGenre: {self.genre} \nOrigin: {self.origin} \nMain character_s: {self.main_character}"

    def __getstate__(self) -> dict:
        state = {}
        state["name"] = self.name
        state["genre"] = self.genre
        state["origin"] = self.origin
        state["main_character"] = self.main_character
        return state

    def __setstate__(self, state: dict):
        self.name = state["name"]
        self.genre = state["genre"]
        self.origin = state["origin"]
        self.main_character = state["main_character"]


parser = argparse.ArgumentParser(description='Parser. Just a parser.')
parser.add_argument('-f', '--file_s_name', default='default.ini', nargs='?')
parser.add_argument('-p', '--path', help="Here's the path to your file")
args = parser.parse_args()
print(args)
print('\n')

if os.path.exists(args.file_s_name):
    config = configparser.ConfigParser()
    config.read(args.file_s_name, encoding="UTF-8")
    cartoon1 = Cartoon(config["CARTOON1S INFO"]["name"],
                       config["CARTOON1S INFO"]["genre"],
                       config["CARTOON1S INFO"]["origin"],
                       config["CARTOON1S INFO"]["main_character"])
    cartoon2 = Cartoon(config["CARTOON2S INFO"]["name"],
                       config["CARTOON2S INFO"]["genre"],
                       config["CARTOON2S INFO"]["origin"],
                       config["CARTOON2S INFO"]["main_character"])
    serd1 = pickle.dumps(cartoon1)
    with open("file_serd1.txt", "wb") as f:
        f.write(serd1)
    de_serd1 = pickle.loads(serd1)
    with open("file_serd1.txt", "rb") as f:
        content = f.read()
        print(de_serd1)

    print('\n')

    serd2 = pickle.dumps(cartoon2)
    with open("file_serd2.txt", "wb") as f:
        f.write(serd2)
    de_serd2 = pickle.loads(serd2)
    with open("file_serd2.txt", "rb") as f:
        content = f.read()
        print(de_serd2)
else:
    print("\nSorry, but your file doesn't exist")