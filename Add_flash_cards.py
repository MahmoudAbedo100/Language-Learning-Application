from googletrans import Translator

translator = Translator()

word_en = input("Type a word in english to get the french translation: ")
word_fr = translator.translate(word_en, src="en", dest="fr").text
print(word_fr)