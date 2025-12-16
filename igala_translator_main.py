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

while True:
    key = input("Enter an English word (or type 'exit' to quit): ").lower()

    if key == "exit":
        print("Goodbye!")
        break

    if key in igala_dictionary:
        print(key, "means", igala_dictionary[key])
    else:
        print("Sorry, word not found.")
