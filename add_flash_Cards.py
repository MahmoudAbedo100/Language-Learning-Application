from googletrans import Translator
import os
import ast

translator = Translator()
cards = []
file_name = "flash_cards.txt"


def retrieve_cards_from_file():
    cards = []
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            cards = ast.literal_eval(f.read())  # gets back real list
    return cards

def display_cards(cards):
    print("The current card list contains " + str(len(cards)) + " cards.")
    for i, card in enumerate(cards):
        print(str(i+1) + ". " + card[0] + ": " + card[1])



def translate_word(word_en):
    word_fr = translator.translate(word_en, src="en", dest="fr").text
    return word_fr


def create_new_card():
    global cards
    word_en = input("Type a word in english to get the french translation: ")
    word_fr = translate_word(word_en)
    new_card = (word_en, word_fr)
    print(new_card)
    answer = input("do you want to save this card? (yes/no) ")
    if answer == "yes":
        cards.append(new_card)


def save_cards_to_file():
    answer = input("save cards to file? (yes/no) ")
    if answer == "yes":
        print("Saving cards...")
        with open(file_name, "w") as f:
            f.write(str(cards))


cards = retrieve_cards_from_file()
display_cards(cards)

while True:
    create_new_card()
    answer = input("do you want to translate another word? (yes/no) ")
    if answer == "no":
        break

print(cards)
save_cards_to_file()
print("End of program.")
