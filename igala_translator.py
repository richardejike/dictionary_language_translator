igala_dictionary = {
    "book": "otakada",
    "water": "omi ofo",
    "food": "ujenwu",
    "drink": "omi",
    "clothe": "ukpo",
    "house": "unyi",
    "bag": "ikpa",
    "cap": "otajiya",
    "shoe": "eda",
    "light": "ugane",
    "door": "alugbona",
    "car": "motokeke",
    "rain": "omi ojale",
    "hand": "owo",
    "head": "oji",
    "happy": "edo ebo",
    "sad": "edo ekpbie",
    "bed": "ate",
    "cold": "eridodo",
    "heat": "utola"
}

def translate_to_igala(word):
    word = word.lower()

if word in igala_dictionary:
    return igala_dictionary[word]
else:
    return "Word not found in the Igala dictionary."

print("English to Igala Dictionary Translator")
print("------------------------------------")

while True:
    english_word = input("Enter an English word (or type 'exit' to quit): ")
    
if english_word.lower() == "exit":
    print("Thank you for using the translator.")
    break

igala_word = translate_to_igala(english_word)

print("Igala meaning:", igala_word)
print()
